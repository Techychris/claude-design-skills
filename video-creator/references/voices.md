# Voice Guide

The goal is always the same: narration the listener doesn't notice as synthetic. Pick by content type, then tune rate/pitch, then fix any words the voice stumbles on.

## Recommended edge-tts voices

Run `edge-tts --list-voices` for the full catalog (hundreds of voices, 70+ languages). These are the consistently engaging picks. The "Multilingual" voices are Microsoft's newest generation and noticeably more expressive than older Neural voices — prefer them for English.

### English
| Voice | Sound | Best for |
|---|---|---|
| en-US-AndrewMultilingualNeural | Warm, confident, conversational male | Default narrator; explainers, tech, business |
| en-US-AvaMultilingualNeural | Bright, expressive, energetic female | Marketing, social media, product launches |
| en-US-BrianMultilingualNeural | Relaxed, casual male | Tutorials, vlogs, calm walkthroughs |
| en-US-EmmaMultilingualNeural | Friendly, articulate female | Education, onboarding, demos |
| en-US-GuyNeural | Newscaster male | News-style, announcements |
| en-US-AriaNeural | Polished, professional female | Corporate, formal |
| en-GB-RyanNeural | British male, measured | Documentary, premium-brand tone |
| en-GB-SoniaNeural | British female, crisp | Luxury, lifestyle |
| en-AU-NatashaNeural | Australian female, friendly | Casual, approachable |

### Other major languages (same pattern exists per locale)
es-MX-DaliaNeural, es-ES-AlvaroNeural, fr-FR-VivienneMultilingualNeural, fr-FR-RemyMultilingualNeural, de-DE-SeraphinaMultilingualNeural, de-DE-FlorianMultilingualNeural, pt-BR-ThalitaMultilingualNeural, ja-JP-NanamiNeural, zh-CN-XiaoxiaoNeural, hi-IN-SwaraNeural, ar-SA-ZariyahNeural, it-IT-IsabellaNeural, ko-KR-SunHiNeural.

## Tuning delivery

- **Rate**: tune to a measured target, not by ear alone. Benchmark: 140–160 WPM gross for narration/explainers; 160+ only for dense social cuts. The Multilingual voices articulate fast — Andrew at default rate measures ~173 WPM gross on conversational copy, so `--rate="-8%"` typically lands explainers at ~155 WPM. Verify after generating: `words ÷ duration × 60` from `timings.json`.
- **Pitch**: small moves only — `"+2Hz"` adds brightness, `"-2Hz"` adds gravity. Beyond ±5Hz sounds processed.
- **Volume**: leave at default; normalize in ffmpeg instead (`loudnorm` filter) if needed.
- **Pacing** (between sentences): handled by `tts_generate.py --pacing human` (default). If a specific spot needs a longer beat than punctuation gives, split it into its own scene, or end the line with "…" — the pacing engine gives ellipses the longest pause. For an extra-deliberate documentary feel, combine `--rate "-5%"` with the default pacing.

## Fixing pronunciation problems

The voice reads what you write, so fix issues in the text:
- Acronyms: "SQL" → "sequel" or "S Q L" (with spaces) depending on intent; "AI" is fine as-is.
- Numbers: "2026" → "twenty twenty-six" if it's a year; "$1.2B" → "one point two billion dollars".
- URLs/emails: "claude.ai" → "claude dot A I".
- A word getting swallowed or rushed: add a comma before it, or an em-dash for a real pause.
- Wrong emphasis in a sentence: restructure so the key word lands at the end of a clause.

## Multi-voice dialogue

For interview or dialogue formats, set `"voice"` per scene in `scenes.json` (the tts_generate.py script supports per-scene overrides). Pair voices with clearly different timbres (e.g., Andrew + Ava). Keep one narrator voice for everything else — switching voices mid-narration is disorienting.

## Local fallback: Kokoro-82M

When the network path is unavailable or the user requires fully offline/owned inference:

```bash
apt-get install -y espeak-ng
pip install kokoro soundfile --break-system-packages   # pulls torch; slow install
```

```python
from kokoro import KPipeline
import soundfile as sf
import numpy as np

pipeline = KPipeline(lang_code='a')  # 'a' American English, 'b' British
chunks = [audio for _, _, audio in pipeline(text, voice='af_heart')]
sf.write('out.wav', np.concatenate(chunks), 24000)
```

Best Kokoro voices: `af_heart`, `af_bella` (female), `am_michael`, `am_fenrir` (male). Quality is excellent for an 82M model; the tradeoff vs edge-tts is no word-boundary timestamps (estimate caption timing per chunk instead) and a heavier install.

## Voice-coach validation (run before final assembly)

Run `python scripts/qa_validate.py --audio-dir audio/` — it computes all the metrics below from `timings.json` plus pitch analysis and prints a PASS/FAIL table (exits non-zero on any fail). Manual reference for what it checks:

| Metric | How | Pass band |
|---|---|---|
| Gross WPM | total words ÷ total duration × 60 | 140–165 (explainer); 120–140 (tutorial/e-learning) |
| Articulation rate | syllables ÷ speaking time (pauses excluded) | 3.5–6.5 syll/sec (normal adult connected speech) |
| Pause ratio | (duration − Σ word spans) ÷ duration | 15–30% |
| Pause variety | SD of inter-word gaps > 0.15s | ≥ 0.08s (uniform gaps sound robotic) |
| Pitch variation | SD of f0 in semitones around the median (parselmouth, floor 70Hz, ceiling 350Hz) | ≥ 3 st (below ~2 st reads as monotone) |

If WPM is high, lower `--rate`; if pause ratio is low, the script has too few sentence breaks — split long sentences. Re-render only the failing scenes.

### Clinical voice-quality check (`--clinical`) — informational

`qa_validate.py --clinical --voice <voice>` synthesizes a sustained vowel, decodes it to lossless WAV (MP3 compression inflates perturbation), and measures jitter (<1.04%), shimmer (<3.81%), and HNR (>20 dB) — the standard sustained-vowel norms clinicians use. **These are not a pass/fail gate for TTS.** Synthetic narration over connected speech runs 2–4× higher on jitter/shimmer by design, and a perfectly clean voice would sound more robotic, not less. Use this only to A/B voices (a voice with lower perturbation on the held vowel tends to sound slightly clearer) or to satisfy a reviewer who asks for clinical metrics.
