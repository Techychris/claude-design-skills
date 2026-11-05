---
name: video-creator
description: Create narrated videos (MP4) with engaging, natural-sounding AI voiceover — never robotic. Use this skill whenever the user asks to make a video, explainer, video presentation, narrated slideshow, voiceover, video ad, social clip, tutorial video, or wants to "turn this into a video", add narration/voice to anything, or convert a script/article/deck into video. Also use it when the user only asks for narration audio or a voiceover track. Covers script writing for spoken delivery, neural TTS voice selection, synced captions, visuals, and ffmpeg assembly.
---

# Video Creator

Build narrated MP4 videos with natural neural voices, synced captions, and clean motion graphics. The pipeline is: **script → narration audio (per scene) → visuals (sized to audio) → assemble with ffmpeg**.

Sound quality is decided twice: once by the voice model, and once by the words you feed it. Both matter equally.

## Step 0: Environment setup (always run first)

```bash
bash scripts/setup_env.sh
```

This installs `edge-tts` and `pillow`, and applies a critical fix: **edge-tts builds its SSL context from certifi's CA bundle, which doesn't trust sandboxed egress proxies.** The script appends the system CA store to certifi's bundle. Without this, every synthesis call fails with `SSL: CERTIFICATE_VERIFY_FAILED`. ffmpeg is preinstalled in this environment — verify with `which ffmpeg` and never reinstall it.

## Step 1: Write a script that sounds human

A perfect voice reading robotic prose still sounds robotic. Before any synthesis, rewrite the content for the ear, not the eye:

- Use contractions everywhere: "it's", "you'll", "don't". Written-out forms ("it is", "you will") are the single biggest tell of machine narration.
- Short sentences, varied rhythm. Mix a 4-word punch with a longer flowing line. Never three long sentences in a row.
- Address the listener: "you", "your", rhetorical questions ("So what does that mean?").
- Add natural connectors and breath points: "Now,", "Here's the thing —", "And honestly?".
- Spell out anything ambiguous: numbers in context ("twenty twenty-six", "$4.5M" → "four and a half million dollars"), acronyms on first use, URLs as words.
- Punctuation is prosody. Commas, em-dashes, and ellipses create pauses; question marks lift intonation; exclamation points add energy (use sparingly).
- 150 words ≈ 1 minute of narration. A 60-second video is ~140–160 words.

Structure the script as **scenes**: one idea per scene, 1–3 sentences each. Scenes become the unit for audio, visuals, and timing.

## Step 2: Generate narration with edge-tts

Default engine: **edge-tts** (Microsoft neural voices — free, no API key, genuinely natural). Generate audio **per scene**, not as one block — per-scene files give exact durations to size visuals against.

```bash
python scripts/tts_generate.py scenes.json --voice en-US-AndrewMultilingualNeural --outdir audio/
```

`scenes.json` is `[{"id": "scene1", "text": "..."}, ...]`. The script writes one MP3 per scene plus `timings.json` (durations + word boundaries for captions).

**Human pacing is on by default**: the script synthesizes each sentence separately, trims the service's flat trailing silence, and rejoins sentences with natural breath pauses — longer after questions and exclamations, slightly jittered so the rhythm never sounds metronomic. The voice's cadence *within* sentences is untouched. Pass `--pacing off` only if the user wants continuous unbroken delivery (e.g., fast-paced ad reads).

**Top voice picks** (full guide with tuning in `references/voices.md` — read it when choosing):

| Voice | Character | Good for |
|---|---|---|
| en-US-AndrewMultilingualNeural | Warm, confident male | Explainers, tech, default pick |
| en-US-AvaMultilingualNeural | Bright, expressive female | Marketing, social, upbeat |
| en-US-BrianMultilingualNeural | Calm, casual male | Tutorials, calm narration |
| en-US-EmmaMultilingualNeural | Friendly, clear female | Education, product demos |
| en-GB-RyanNeural | British male | Documentary tone |

Tune `--rate` by *measured* speed, not feel: target 140–160 WPM gross for explainers (the engagement sweet spot). Andrew/Ava run hot at default (~170+ WPM), so explainers usually need `--rate="-8%"` (note the `=` — argparse requires it for negative values); reserve `+0%` for high-energy social cuts. After generating, compute WPM from `timings.json` (total words ÷ total duration × 60) and adjust if outside the band. Keep one voice per video unless doing dialogue.

**Fallback — local Kokoro-82M** (Apache 2.0, runs on CPU, excellent prosody) if the network path fails or the user wants fully offline: `pip install kokoro soundfile --break-system-packages && apt-get install -y espeak-ng`, then use `KPipeline(lang_code='a')` with voice `af_heart` or `am_michael`. Heavier install (pulls torch), so only reach for it when edge-tts isn't viable.

**Always listen-check**: after generating, spot-check durations look sane (`timings.json`) and present at least the first audio file to the user early if the video is long — voice choice is subjective and cheap to change before assembly.

## Step 2.5: QA-validate the narration

Before building visuals, run the QA gate on the generated audio:

```bash
python scripts/qa_validate.py --audio-dir audio/
```

It scores five delivery metrics against benchmarks — gross WPM (140–165), articulation rate (3.5–6.5 syll/sec), pause ratio (15–30%), pause variety, and pitch variation — prints a PASS/FAIL table, and exits non-zero if any fail, with a specific fix for each (e.g. "lower --rate", "try a more expressive voice"). Re-render only the scenes that need it, then re-run. Don't proceed to assembly until delivery passes.

Add `--clinical --voice <voice>` for an optional clinical voice-quality read (jitter/shimmer/HNR on a lossless sustained vowel). This is **informational only**: synthetic voices don't meet human sustained-vowel norms and shouldn't — a little perturbation is what keeps narration from sounding robotic. Use it to compare voices, not as a gate. See `references/voices.md` for what the numbers mean.

## Step 3: Build visuals sized to the audio

Each scene's visual duration = its audio duration + ~0.4s breathing room. Options, in order of typical fit:

1. **Motion-graphic slides** (default): render 1920×1080 PNGs with Pillow — bold headline, supporting line, accent color, generous whitespace — then animate with ffmpeg `zoompan` (slow Ken Burns zoom makes static frames feel alive).
2. **Charts**: matplotlib with large fonts (title ≥ 40pt) on a dark or brand background.
3. **User-supplied images/footage**: scale and pad to 1920×1080 (`scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2`).

Design rules and ready-to-use ffmpeg recipes (Ken Burns, crossfades, captions, music ducking) are in `references/visuals.md` — read it before assembling.

## Step 4: Assemble

```bash
python scripts/assemble_video.py scenes.json --audio-dir audio/ --images-dir images/ -o video.mp4
```

The script turns each scene's PNG + MP3 into a clip (with Ken Burns motion), concatenates with crossfades, muxes the narration, and optionally burns in captions from the word timings (`--captions`). Output: H.264 + AAC MP4, `yuv420p` (required for universal playback), 30fps.

For anything the script doesn't cover (vertical 9:16, background music, video footage), use the recipes in `references/visuals.md` directly.

## Step 5: Deliver

Copy the final MP4 to `/mnt/user-data/outputs/` and present it with `present_files`. For videos over ~90s, also present the script text so the user can request line edits, and offer to re-render individual scenes (per-scene files make this cheap — never re-synthesize the whole video for a one-line change).

## Pitfalls

- `SSL: CERTIFICATE_VERIFY_FAILED` from edge-tts → the certifi CA fix in `setup_env.sh` wasn't applied.
- Video plays without sound in some players → missing `-pix_fmt yuv420p` or audio not AAC.
- Odd dimensions crash H.264 → width and height must be even numbers.
- Robotic-sounding output with a good voice → the script is the problem; rewrite per Step 1.
- edge-tts is an online service: batch politely (the helper script throttles slightly between scenes) and don't parallelize aggressively.
- Drifting captions → always use the word boundaries edge-tts emits (captured in `timings.json`), never estimate timing from word counts.
