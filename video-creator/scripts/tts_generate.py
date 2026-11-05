#!/usr/bin/env python3
"""Generate per-scene narration with edge-tts, with human pacing and word timings.

Usage:
    python tts_generate.py scenes.json --voice en-US-AndrewMultilingualNeural \
        --rate "+8%" --outdir audio/ [--pacing human|off]

scenes.json format:
    [{"id": "scene1", "text": "Hey there! ..."},
     {"id": "scene2", "text": "...", "voice": "en-US-AvaMultilingualNeural"}]
    (per-scene "voice"/"rate"/"pitch" keys override the CLI defaults)

Pacing (default "human"): each sentence is synthesized separately, then the
sentences are rejoined with natural breath pauses — longer after questions and
exclamations, slightly varied so the rhythm never sounds metronomic. The
voice's cadence WITHIN sentences is untouched. Use --pacing off to synthesize
each scene as one continuous block.

Outputs:
    <outdir>/<id>.mp3 per scene
    <outdir>/timings.json: {"<id>": {"duration": float_seconds,
                                     "words": [{"text", "start", "end"}, ...]}}
"""
import argparse, asyncio, json, random, re, subprocess, sys, tempfile
from pathlib import Path

import edge_tts

SAMPLE_RATE = 24000  # edge-tts native rate


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True)
    return float(out.stdout.strip())


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg failed:\n{r.stderr[-1500:]}")


def split_sentences(text: str):
    """Split on sentence-ending punctuation, keeping the punctuation attached."""
    parts = re.split(r"(?<=[.!?\u2026])\s+", text.strip())
    return [p for p in parts if p]


def breath_pause(sentence: str, rng: random.Random) -> float:
    """Pause to insert AFTER this sentence. Questions and exclamations get a
    beat to land; jitter keeps the rhythm organic."""
    end = sentence.rstrip()[-1] if sentence.rstrip() else "."
    base = {"?": 0.55, "!": 0.50, "\u2026": 0.60}.get(end, 0.38)
    return max(0.15, base + rng.uniform(-0.07, 0.07))


async def synth_piece(text, voice, rate, pitch, mp3_path: Path):
    """Synthesize one piece of text, returning its word boundaries."""
    words = []
    try:
        comm = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch,
                                    boundary="WordBoundary")
    except TypeError:  # older edge-tts without the boundary kwarg
        comm = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    with open(mp3_path, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 1e7
                words.append({"text": chunk["text"],
                              "start": round(start, 3),
                              "end": round(start + chunk["duration"] / 1e7, 3)})
    return words


async def synth_with_retry(text, voice, rate, pitch, mp3_path: Path):
    for attempt in range(3):
        try:
            return await synth_piece(text, voice, rate, pitch, mp3_path)
        except Exception as e:
            if attempt == 2:
                print(f"FAILED: {e}", file=sys.stderr)
                raise
            await asyncio.sleep(2 * (attempt + 1))


def make_silence(path: Path, seconds: float):
    run(["ffmpeg", "-y", "-f", "lavfi",
         "-i", f"anullsrc=r={SAMPLE_RATE}:cl=mono",
         "-t", f"{seconds:.3f}", "-c:a", "pcm_s16le", path])


def to_wav(mp3: Path, wav: Path):
    run(["ffmpeg", "-y", "-i", mp3, "-ar", str(SAMPLE_RATE), "-ac", "1",
         "-c:a", "pcm_s16le", wav])


async def build_scene(scene, args, outdir: Path):
    voice = scene.get("voice", args.voice)
    rate = scene.get("rate", args.rate)
    pitch = scene.get("pitch", args.pitch)
    final_mp3 = outdir / f"{scene['id']}.mp3"

    if args.pacing == "off":
        words = await synth_with_retry(scene["text"], voice, rate, pitch, final_mp3)
        return words

    sentences = split_sentences(scene["text"])
    if len(sentences) <= 1:
        words = await synth_with_retry(scene["text"], voice, rate, pitch, final_mp3)
        return words

    rng = random.Random(scene["id"])  # reproducible per scene
    tmp = Path(tempfile.mkdtemp())
    pieces, words, t = [], [], 0.0

    for i, sent in enumerate(sentences):
        mp3 = tmp / f"s{i}.mp3"
        wav = tmp / f"s{i}.wav"
        sent_words = await synth_with_retry(sent, voice, rate, pitch, mp3)
        to_wav(mp3, wav)
        dur = probe_duration(wav)
        # Trim edge-tts's trailing service silence so our pauses are the only gaps
        trimmed = tmp / f"s{i}_t.wav"
        run(["ffmpeg", "-y", "-i", wav, "-af",
             "areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse",
             trimmed])
        dur = probe_duration(trimmed)
        pieces.append(trimmed)
        for wd in sent_words:
            words.append({"text": wd["text"],
                          "start": round(t + wd["start"], 3),
                          "end": round(t + min(wd["end"], dur), 3)})
        t += dur
        if i < len(sentences) - 1:
            gap = breath_pause(sent, rng)
            sil = tmp / f"g{i}.wav"
            make_silence(sil, gap)
            pieces.append(sil)
            t += gap
        await asyncio.sleep(0.3)  # be polite to the free service

    concat = tmp / "list.txt"
    concat.write_text("".join(f"file '{p}'\n" for p in pieces))
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat,
         "-c:a", "libmp3lame", "-q:a", "2", final_mp3])
    return words


async def main():
    p = argparse.ArgumentParser()
    p.add_argument("scenes_json")
    p.add_argument("--voice", default="en-US-AndrewMultilingualNeural")
    p.add_argument("--rate", default="+0%")
    p.add_argument("--pitch", default="+0Hz")
    p.add_argument("--outdir", default="audio")
    p.add_argument("--pacing", choices=["human", "off"], default="human")
    args = p.parse_args()

    scenes = json.loads(Path(args.scenes_json).read_text())
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    timings = {}
    for i, scene in enumerate(scenes):
        words = await build_scene(scene, args, outdir)
        dur = probe_duration(outdir / f"{scene['id']}.mp3")
        timings[scene["id"]] = {"duration": round(dur, 3), "words": words}
        print(f"  {scene['id']}: {dur:.1f}s ({len(words)} words)")
        if i < len(scenes) - 1:
            await asyncio.sleep(0.5)

    (outdir / "timings.json").write_text(json.dumps(timings, indent=2))
    total = sum(t["duration"] for t in timings.values())
    print(f"Done. {len(scenes)} scenes, {total:.1f}s total narration.")


if __name__ == "__main__":
    asyncio.run(main())
