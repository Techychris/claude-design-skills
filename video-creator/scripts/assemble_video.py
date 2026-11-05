#!/usr/bin/env python3
"""Assemble per-scene PNGs + MP3s into a final narrated MP4.

Usage:
    python assemble_video.py scenes.json --audio-dir audio/ --images-dir images/ \
        -o video.mp4 [--captions] [--no-motion] [--size 1920x1080]

Expects:
    audio/<id>.mp3 and audio/timings.json (from tts_generate.py)
    images/<id>.png (1920x1080 or matching --size)

Each scene clip = image with slow Ken Burns zoom, lasting audio duration + 0.4s.
Clips are concatenated, narration is concatenated with matching gaps, and
optionally word-synced captions are burned in.
"""
import argparse, json, subprocess, tempfile
from pathlib import Path

PAD = 0.4  # seconds of visual breathing room after each scene's narration
FPS = 30


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"Command failed:\n{' '.join(map(str, cmd))}\n{r.stderr[-2000:]}")


def fmt_srt_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):06.3f}".replace(".", ",")


def build_captions(scenes, timings, offsets, srt_path, group=4):
    """Group word boundaries into short caption chunks, offset to video time.
    Breaks early at sentence-ending punctuation so captions don't straddle sentences."""
    entries, n = [], 1
    for scene in scenes:
        words = timings[scene["id"]]["words"]
        off = offsets[scene["id"]]
        chunk = []
        for w in words:
            chunk.append(w)
            if len(chunk) >= group or w["text"].rstrip().endswith((".", "!", "?", ":")):
                entries.append((n, off + chunk[0]["start"], off + chunk[-1]["end"],
                                " ".join(x["text"] for x in chunk)))
                n += 1
                chunk = []
        if chunk:
            entries.append((n, off + chunk[0]["start"], off + chunk[-1]["end"],
                            " ".join(x["text"] for x in chunk)))
            n += 1
    srt_path.write_text("\n".join(
        f"{i}\n{fmt_srt_time(a)} --> {fmt_srt_time(b)}\n{txt}\n"
        for i, a, b, txt in entries))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("scenes_json")
    p.add_argument("--audio-dir", default="audio")
    p.add_argument("--images-dir", default="images")
    p.add_argument("-o", "--output", default="video.mp4")
    p.add_argument("--captions", action="store_true")
    p.add_argument("--no-motion", action="store_true", help="disable Ken Burns zoom")
    p.add_argument("--size", default="1920x1080")
    args = p.parse_args()

    w, h = map(int, args.size.split("x"))
    w, h = w - w % 2, h - h % 2  # H.264 needs even dims
    scenes = json.loads(Path(args.scenes_json).read_text())
    adir, idir = Path(args.audio_dir), Path(args.images_dir)
    timings = json.loads((adir / "timings.json").read_text())

    tmp = Path(tempfile.mkdtemp())
    clip_list, audio_list = [], []
    offsets, t = {}, 0.0

    for scene in scenes:
        sid = scene["id"]
        dur = timings[sid]["duration"] + PAD
        offsets[sid] = t
        t += dur
        frames = int(dur * FPS)
        clip = tmp / f"{sid}.mp4"

        if args.no_motion:
            vf = f"scale={w}:{h},format=yuv420p"
        else:
            # Render zoompan at 2x then downscale: hides zoompan's jitter artifacts.
            vf = (f"scale={w*2}:{h*2},"
                  f"zoompan=z='1+0.0008*on':d={frames}:s={w}x{h}:fps={FPS}"
                  f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)',format=yuv420p")
        run(["ffmpeg", "-y", "-loop", "1", "-i", idir / f"{sid}.png",
             "-vf", vf, "-t", f"{dur:.3f}", "-r", str(FPS),
             "-c:v", "libx264", "-preset", "fast", "-an", clip])
        clip_list.append(clip)

        # Pad each scene's audio with PAD seconds of silence so audio/video stay aligned
        padded = tmp / f"{sid}_padded.m4a"
        run(["ffmpeg", "-y", "-i", adir / f"{sid}.mp3",
             "-af", f"apad=pad_dur={PAD}", "-c:a", "aac", "-b:a", "192k", padded])
        audio_list.append(padded)

    concat_v = tmp / "video_list.txt"
    concat_v.write_text("".join(f"file '{c}'\n" for c in clip_list))
    concat_a = tmp / "audio_list.txt"
    concat_a.write_text("".join(f"file '{a}'\n" for a in audio_list))

    silent = tmp / "silent.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_v, "-c", "copy", silent])
    narration = tmp / "narration.m4a"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_a, "-c", "copy", narration])

    out = Path(args.output)
    if args.captions:
        srt = tmp / "captions.srt"
        build_captions(scenes, timings, offsets, srt)
        style = ("FontSize=14,Bold=1,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,"
                 "Outline=2,MarginV=40")
        run(["ffmpeg", "-y", "-i", silent, "-i", narration,
             "-vf", f"subtitles={srt}:force_style='{style}'",
             "-c:v", "libx264", "-preset", "fast", "-pix_fmt", "yuv420p",
             "-c:a", "copy", "-shortest", out])
    else:
        run(["ffmpeg", "-y", "-i", silent, "-i", narration,
             "-c:v", "copy", "-c:a", "copy", "-shortest", out])

    print(f"Wrote {out} ({t:.1f}s, {len(scenes)} scenes)")


if __name__ == "__main__":
    main()
