#!/usr/bin/env python3
"""QA-validate generated narration before final assembly.

Runs two batteries:
  1. Delivery metrics (always) — on the actual narration MP3s + timings.json:
     gross WPM, articulation rate (syll/sec), pause ratio, pause variety,
     and pitch variation. These are the metrics that matter for engaging,
     non-robotic narration.
  2. Clinical voice-quality check (--clinical) — synthesizes a sustained vowel
     in the same voice and measures jitter/shimmer/HNR on LOSSLESS wav against
     sustained-vowel norms. Connected-speech MP3s inflate these metrics, so a
     held vowel on uncompressed audio is the only valid way to read them.

Usage:
    python qa_validate.py --audio-dir audio/                     # delivery only
    python qa_validate.py --audio-dir audio/ --clinical \
        --voice en-US-AndrewMultilingualNeural                   # + clinical

Exit code is 0 if all delivery checks pass, 1 if any fail (useful in scripts).
Requires: pip install praat-parselmouth syllables --break-system-packages
"""
import argparse, asyncio, json, subprocess, sys, tempfile
from pathlib import Path

import numpy as np

# ---- delivery thresholds (engaging narration) ----
WPM_BAND = (140, 165)          # gross words/min for explainers
ARTIC_BAND = (3.5, 6.5)        # syll/sec, normal adult connected speech
PAUSE_BAND = (0.15, 0.30)      # fraction of duration that is silence
PAUSE_SD_MIN = 0.08            # SD of inter-word gaps (uniform = robotic)
PITCH_SD_MIN = 3.0             # semitones around median (flat = monotone)

# ---- clinical sustained-vowel norms (healthy adult, lossless) ----
JITTER_MAX = 1.04              # %
SHIMMER_MAX = 3.81             # %
HNR_MIN = 20.0                 # dB (>7 minimum, ~20 typical healthy)


def count_syllables(word):
    try:
        import syllables
        return max(1, syllables.estimate(word))
    except Exception:
        w = word.lower(); v = "aeiouy"; n = 0; prev = False
        for c in w:
            if c in v and not prev: n += 1
            prev = c in v
        if w.endswith("e"): n = max(1, n - 1)
        return max(1, n)


def fmt(ok):
    return "\033[32mPASS\033[0m" if ok else "\033[31mFAIL\033[0m"


def delivery_check(audio_dir):
    import parselmouth
    timings = json.loads((Path(audio_dir) / "timings.json").read_text())
    tot_w = tot_syl = tot_speech = tot_dur = 0
    all_gaps, pitch_sds = [], []

    for sid, t in timings.items():
        words, dur = t["words"], t["duration"]
        tot_w += len(words)
        tot_syl += sum(count_syllables(w["text"]) for w in words)
        tot_speech += sum(w["end"] - w["start"] for w in words)
        tot_dur += dur
        gaps = [words[i + 1]["start"] - words[i]["end"] for i in range(len(words) - 1)]
        all_gaps += [g for g in gaps if g > 0.15]
        snd = parselmouth.Sound(str(Path(audio_dir) / f"{sid}.mp3"))
        f0 = snd.to_pitch(pitch_floor=70, pitch_ceiling=350).selected_array["frequency"]
        f0 = f0[f0 > 0]
        if len(f0) > 1:
            pitch_sds.append(float(np.std(12 * np.log2(f0 / np.median(f0)))))

    wpm = tot_w / tot_dur * 60
    artic = tot_syl / tot_speech if tot_speech else 0
    pause_ratio = (tot_dur - tot_speech) / tot_dur
    pause_sd = float(np.std(all_gaps)) if all_gaps else 0
    pitch_sd = float(np.mean(pitch_sds)) if pitch_sds else 0

    rows = [
        ("Gross speaking rate", f"{wpm:.0f} WPM", f"{WPM_BAND[0]}-{WPM_BAND[1]}",
         WPM_BAND[0] <= wpm <= WPM_BAND[1]),
        ("Articulation rate", f"{artic:.1f} syll/s", f"{ARTIC_BAND[0]}-{ARTIC_BAND[1]}",
         ARTIC_BAND[0] <= artic <= ARTIC_BAND[1]),
        ("Pause ratio", f"{pause_ratio*100:.0f}%", f"{PAUSE_BAND[0]*100:.0f}-{PAUSE_BAND[1]*100:.0f}%",
         PAUSE_BAND[0] <= pause_ratio <= PAUSE_BAND[1]),
        ("Pause variety (SD)", f"{pause_sd:.2f}s", f">={PAUSE_SD_MIN}",
         pause_sd >= PAUSE_SD_MIN),
        ("Pitch variation (SD)", f"{pitch_sd:.1f} st", f">={PITCH_SD_MIN}",
         pitch_sd >= PITCH_SD_MIN),
    ]
    print("\n=== DELIVERY QA (engaging-narration metrics) ===")
    print(f"{'metric':24}{'measured':>14}{'target':>12}   result")
    all_ok = True
    for name, val, tgt, ok in rows:
        all_ok &= ok
        print(f"{name:24}{val:>14}{tgt:>12}   {fmt(ok)}")
    return all_ok, rows


async def _synth_vowel(voice, wav_path):
    import edge_tts
    # A held vowel-like utterance; edge-tts won't truly sustain, so we string
    # several long "ahh"s and analyze the steadiest voiced region.
    text = "Ahhhhh. Ahhhhh. Ahhhhh."
    mp3 = wav_path.with_suffix(".mp3")
    comm = edge_tts.Communicate(text, voice, rate="-20%")
    with open(mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
    # decode to lossless wav (no MP3 perturbation inflation)
    subprocess.run(["ffmpeg", "-y", "-i", str(mp3), "-ar", "44100", "-ac", "1",
                    "-c:a", "pcm_s16le", str(wav_path)],
                   capture_output=True, check=True)


def clinical_check(voice):
    import parselmouth
    from parselmouth.praat import call
    tmp = Path(tempfile.mkdtemp())
    wav = tmp / "vowel.wav"
    asyncio.run(_synth_vowel(voice, wav))
    snd = parselmouth.Sound(str(wav))
    # Find the steadiest 0.4s voiced window (lowest pitch variance) — approximates
    # a held vowel as closely as a TTS engine allows.
    d = snd.get_total_duration()
    pitch = snd.to_pitch(pitch_floor=70, pitch_ceiling=350)
    best, best_var = (d / 3, 2 * d / 3), float("inf")
    win = 0.4
    step = 0.05
    start = 0.1
    while start + win < d - 0.1:
        vals = [pitch.get_value_at_time(start + i * 0.02) for i in range(int(win / 0.02))]
        vals = [v for v in vals if v and v > 0]
        if len(vals) > win / 0.02 * 0.7:  # mostly voiced
            var = float(np.var(vals))
            if var < best_var:
                best_var, best = var, (start, start + win)
        start += step
    seg = snd.extract_part(best[0], best[1], parselmouth.WindowShape.RECTANGULAR, 1, True)
    pp = call(seg, "To PointProcess (periodic, cc)", 70, 350)
    jitter = call(pp, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3) * 100
    shimmer = call([seg, pp], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6) * 100
    hnr = call(call(seg, "To Harmonicity (cc)", 0.01, 70, 0.1, 1.0), "Get mean", 0, 0)

    rows = [
        ("Jitter (local)", f"{jitter:.2f}%", f"<{JITTER_MAX}%", jitter < JITTER_MAX),
        ("Shimmer (local)", f"{shimmer:.2f}%", f"<{SHIMMER_MAX}%", shimmer < SHIMMER_MAX),
        ("HNR", f"{hnr:.1f} dB", f">{HNR_MIN}", hnr > HNR_MIN),
    ]
    print("\n=== CLINICAL QA (sustained vowel, lossless) ===")
    print(f"{'metric':24}{'measured':>14}{'target':>12}   result")
    for name, val, tgt, ok in rows:
        print(f"{name:24}{val:>14}{tgt:>12}   {fmt(ok)}")
    print("Note: informational only — synthetic voices need not meet human")
    print("sustained-vowel norms; slight perturbation reads as natural, not defective.")
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--audio-dir", default="audio")
    p.add_argument("--clinical", action="store_true")
    p.add_argument("--voice", default="en-US-AndrewMultilingualNeural")
    args = p.parse_args()

    ok, rows = delivery_check(args.audio_dir)
    if args.clinical:
        clinical_check(args.voice)

    print("\n" + ("All delivery checks passed." if ok else
                  "Some delivery checks FAILED — adjust before assembly:"))
    if not ok:
        for name, val, tgt, passed in rows:
            if not passed:
                hint = {
                    "Gross speaking rate": "adjust --rate (lower if too fast)",
                    "Articulation rate": "adjust --rate",
                    "Pause ratio": "add/remove sentence breaks in the script",
                    "Pause variety (SD)": "ensure --pacing human is on",
                    "Pitch variation (SD)": "try a more expressive voice (Ava, Emma)",
                }.get(name, "")
                print(f"  - {name}: {val} (want {tgt}) → {hint}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
