# Visuals & ffmpeg Recipes

## Slide design (Pillow)

Render 1920×1080 PNGs (1080×1920 for vertical). Rules that keep slides from looking like a default deck:

- One idea per slide: a headline (≤ 8 words, 72–110px bold) plus at most one supporting line (36–48px, lower opacity).
- Pick a palette and stick to it: dark background (#0F1117, #1A1A2E) with one accent color reads as "video", white backgrounds read as "slideshow".
- Use a real font: `fc-list | grep -iE "dejavu|liberation"` shows what's installed; DejaVu Sans Bold is reliably present. Load with `ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)`.
- Left-align body text near the left third; center only short titles.
- Add one geometric accent (thin rule under the headline, corner block, large translucent number) so frames aren't pure text.
- Safe margins: keep content ≥ 100px from edges; ≥ 160px from the bottom if burning captions.

```python
from PIL import Image, ImageDraw, ImageFont
img = Image.new("RGB", (1920, 1080), "#0F1117")
d = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 92)
d.text((140, 420), "Headline here", font=font, fill="#FFFFFF")
d.rectangle([140, 560, 460, 572], fill="#4F9CFF")  # accent rule
img.save("images/scene1.png")
```

For charts, use matplotlib with `figsize=(19.2, 10.8), dpi=100`, dark style, and font sizes ≥ 28 — chart text that's readable in a notebook is invisible in a video.

## Core ffmpeg recipes

Always: `-pix_fmt yuv420p` (universal playback), even dimensions, `-r 30`.

**Still image → clip with Ken Burns zoom** (render at 2x then downscale to hide zoompan jitter):
```bash
ffmpeg -y -loop 1 -i scene.png -vf \
  "scale=3840:2160,zoompan=z='1+0.0008*on':d=150:s=1920x1080:fps=30:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)',format=yuv420p" \
  -t 5 -c:v libx264 -preset fast -an clip.mp4
```
Pan instead of zoom: keep `z='1.1'` fixed and animate `x='(iw-iw/zoom)*on/{frames}'`.

**Crossfade between two clips** (0.5s):
```bash
ffmpeg -y -i a.mp4 -i b.mp4 -filter_complex \
  "[0][1]xfade=transition=fade:duration=0.5:offset=PREV_DURATION_MINUS_0.5" out.mp4
```
For many scenes, hard cuts via concat (what assemble_video.py does) are simpler and read fine with motion on each clip; reserve xfade chains for ≤ 5 scenes.

**Fit any image/footage to frame without distortion:**
```bash
-vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=#0F1117"
```

**Burn captions with styling:**
```bash
-vf "subtitles=captions.srt:force_style='FontSize=14,Bold=1,OutlineColour=&H000000,Outline=2,MarginV=40'"
```

**Background music under narration with auto-ducking:**
```bash
ffmpeg -y -i video.mp4 -i music.mp3 -filter_complex \
  "[1:a]volume=0.25,aloop=loop=-1:size=2e9[m];[0:a][m]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[duck];[0:a][duck]amix=inputs=2:duration=first[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -shortest out.mp4
```
Only add music the user supplies or that is verifiably licensed — don't download random tracks.

**Vertical (9:16) for social:** generate 1080×1920 slides, swap all dimensions, keep captions higher (`MarginV=120`) to clear platform UI.

**Normalize final loudness:** append `-af loudnorm=I=-16:TP=-1.5` on the final mux for consistent volume across platforms.

## Fades in and out

Polish for the final cut:
```bash
-vf "fade=t=in:st=0:d=0.6,fade=t=out:st=END_MINUS_0.8:d=0.8" \
-af "afade=t=in:st=0:d=0.4,afade=t=out:st=END_MINUS_0.8:d=0.8"
```
