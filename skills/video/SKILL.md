---
name: video
description: >
  Edit, process, and render videos using FFmpeg and Remotion. Handles stitching, transitions,
  captions, teasers, transcription, title cards, and graphics generation. Supports both
  long-form YouTube (16:9) and YouTube Shorts (9:16).

  USE THIS SKILL WHEN:
  - User mentions video, clip, footage, mp4, mov, avi, mkv, or any video format
  - User wants to combine, stitch, merge, or join video files
  - User asks about transitions, fades, crossfades, or effects between clips
  - User needs captions, subtitles, or word-by-word highlighting
  - User wants a teaser, trailer, Short, or highlight reel from longer video
  - User mentions FFmpeg, ffprobe, Remotion, or related errors
  - User asks about video transcription or whisper speech-to-text
  - User asks about video duration, resolution, fps, or trimming
  - User has .mp4, .mov, .captions.json files or video folders
  - User asks about thumbnails, overlays, title cards, or graphics for video

  TRIGGERS: "video", "edit video", "clip", "footage", "stitch", "captions",
  "subtitles", "teaser", "short", "trailer", "highlight", "ffmpeg", "remotion",
  "transcribe", "thumbnail", "title card", "transitions"
---

# Video Editing Skill

Edits, processes, and renders videos using FFmpeg and Remotion. Optimized for two output formats:
- **Long-form YouTube** (16:9, 1920×1080)
- **YouTube Shorts** (9:16, 1080×1920)

---

## Intelligent Editing Workflow

This skill enables the AI agent to act as a smart video editor. Before executing commands:

1. **Analyze** — Examine videos (duration, resolution, audio) using ffprobe
2. **Transcribe** — Get speech content for smart cuts (if needed)
3. **Ask** — Clarify user intent and preferences
4. **Plan** — Propose edit approach for approval
5. **QA Test** — Run automated tests before user preview (see references/qa-testing.md)
6. **Preview** — Only show to user after QA passes
7. **Iterate** — Refine based on feedback

See references/intelligent-editing.md for detailed workflow, questions to ask, and quality checks.

---

## Tool Selection

| Task | FFmpeg | Remotion |
|------|--------|----------|
| **Stitching** | Same codec, no effects | Transitions, overlays, programmatic |
| **Transitions** | Simple crossfades | Multiple types, custom timing |
| **Captions** | SRT burn-in | Word-by-word highlighting |
| **Teasers/Shorts** | Quick clips | Text overlays, branded elements |
| **Title Cards** | N/A | Animated section headers |
| **Graphics** | Static overlays | Animated thumbnails, end screens |

**General guidance:**
- **FFmpeg**: Fast CLI operations, batch processing, format conversion, simple edits
- **Remotion**: Styled content, animations, preview before render, React components

---

## Output Formats

### Long-Form YouTube
- Resolution: 1920×1080 (16:9)
- Frame rate: 30fps
- Typical length: 10-25 minutes
- Captions: Optional but recommended for accessibility
- Title cards: Between major sections
- End screen: CTA + subscribe prompt

### YouTube Shorts
- Resolution: 1080×1920 (9:16)
- Frame rate: 30fps
- Max length: 60 seconds
- Captions: Required (most Shorts watched without sound initially)
- Fast pacing: 1.3x playback speed for energy
- Hook in first 2 seconds

### Teaser Clips (from long-form → Shorts)
- Pull 3-4 highlight clips from the full video
- Total 25-30 seconds
- Each clip must start with an explicit subject (never pronouns)
- Never start clips with: "But", "And", "So", "Now", "It", "This", "That", "They"
- First clip must NOT overlap with the video intro
- Add word-by-word captions
- Smooth fade transitions (0.4s) between clips

---

## Reference Files

Read these files as needed:

### Intelligence Layer
| File | Contents |
|------|----------|
| references/intelligent-editing.md | Smart editing workflow, questions, quality checks |
| references/video-analysis.md | Analyze videos with ffprobe |
| references/transcription.md | Whisper transcription for speech analysis |
| references/qa-testing.md | **QA tests before user preview** |

### Core Editing
| File | Contents |
|------|----------|
| references/stitching.md | Combine multiple clips into one video |
| references/transitions.md | Add fade, slide, wipe between clips |
| references/captions.md | Add subtitles and word-by-word captions |
| references/teasers.md | Create 30-60 second teasers and Shorts |
| references/title-cards.md | Add chapter headers, bumpers, section titles |
| references/graphics-generation.md | Generate thumbnails, overlays, social graphics |

### Technical Reference
| File | Contents |
|------|----------|
| references/ffmpeg-basics.md | Common FFmpeg patterns and troubleshooting |
| references/remotion-setup.md | Remotion project setup and workflow |
| references/remotion-tips.md | Animations, timing, springs, sequences, and captions |
| references/reference-implementation.md | **Complete working code to recreate the project** |

---

## Quick Start

### Transcription (Fast — GPU Accelerated on Mac M2)
```bash
# 1. Setup whisper.cpp (one-time)
npx ts-node scripts/setup-whisper.ts

# 2. Transcribe all videos (Metal GPU accelerated)
npx ts-node scripts/transcribe-fast.ts
```

### FFmpeg (CLI)
```bash
# Check installation
which ffmpeg || brew install ffmpeg

# Basic concat (same codec)
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4

# Burn in subtitles
ffmpeg -i video.mp4 -vf "subtitles=captions.srt" output.mp4

# Extract audio for transcription
ffmpeg -i video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav
```

### Remotion (React)
```bash
# Start preview (always do this first)
npm run dev

# Render long-form (only when user requests)
npx remotion render FinalVideo out/video.mp4

# Render Short/teaser
npx remotion render TeaserOnly out/teaser.mp4
```

---

## Typical Workflows

### Workflow 1: Full YouTube Video Edit
1. User drops raw clips into project folder
2. Agent analyzes each clip (ffprobe → duration, resolution, codec)
3. Agent transcribes all clips (whisper.cpp)
4. Agent proposes edit plan: clip order, transitions, title card placement
5. User approves plan
6. Agent stitches clips with transitions
7. Agent adds title cards between sections
8. Agent generates captions
9. Agent runs QA tests
10. User previews in Remotion Studio
11. Agent renders final 1080p video

### Workflow 2: Create YouTube Shorts from Long-Form
1. Agent reads transcript of the full video
2. Agent identifies 3-4 strongest standalone moments (clear subject, impactful statement)
3. Agent proposes teaser clip selections with timestamps
4. User approves selections
5. Agent extracts clips, applies 1.3x speed, adds captions
6. Agent renders in 9:16 vertical format
7. User reviews

### Workflow 3: Add Captions to Existing Video
1. Agent transcribes video (whisper.cpp with word-level timestamps)
2. Agent generates caption file (.captions.json)
3. Two options:
   - Simple: Burn SRT subtitles via FFmpeg (fast, basic styling)
   - Styled: Word-by-word highlighting via Remotion (professional, animated)
4. Agent renders captioned video

---

## Key Lessons Learned

### Transcription (IMPORTANT)
- **Use `@remotion/install-whisper-cpp`** — NOT Python whisper (10x faster with GPU)
- Use `base.en` model for speed, `medium.en` for final quality
- **Required parameter**: `whisperCppVersion: '1.5.5'` in transcribe() call
- Enable `tokenLevelTimestamps: true` for word-level captions
- Whisper.cpp uses Metal GPU on Mac M2 — fast local transcription

### Captions
- **Active word**: Yellow `#FFD700`
- **Spoken words**: White `#FFFFFF`
- **Upcoming words**: Light gray `#E0E0E0`
- **Font**: Roboto at 48px for 1080p
- **Black stroke outline** (works on ANY background):
  ```css
  WebkitTextStroke: '3px black',
  paintOrder: 'stroke fill',
  textShadow: '0px 0px 4px rgba(0,0,0,1), 0px 0px 8px rgba(0,0,0,0.8)'
  ```

### Teasers / Shorts
- Never start clips with pronouns or conjunctions
- Each clip must have an explicit subject
- 3-4 clips totaling 25-30 seconds for teasers
- Playback speed: 1.3x for energy (1.5x is too fast)
- Transitions: Smooth fade (0.4s) between clips
- First clip must NOT overlap with intro start

### Remotion Video Trimming
- Use `OffthreadVideo` component
- Set BOTH `startFrom` AND `endAt` props
- Convert ms to frames: `Math.round((ms / 1000) * fps)`

---

## Edge Cases & Gotchas

### File Naming
- Avoid spaces in video filenames: use `intro.mp4` not `Intro Video.mp4`
- Remotion folder names can only contain letters, numbers, and hyphens

### Ports
- Remotion Studio may start on port 3001 if 3000 is in use

### Codec Mismatch
- FFmpeg concat demuxer (`-c copy`) fails silently with mismatched codecs
- Use `ffprobe` to check codecs before concatenating
- Use filter_complex for different codecs/resolutions

### Workflow
- **Always preview in Remotion Studio before rendering**
- Never render automatically — wait for user approval
- Copy videos to `public/` folder for Remotion projects

---

## Mac Mini Setup (One-Time)

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install FFmpeg
brew install ffmpeg

# Install Node.js (for Remotion)
brew install node

# Verify installations
ffmpeg -version
node --version
npm --version

# Create video editing project
mkdir -p ~/video-editor && cd ~/video-editor
npm init -y

# Install Remotion dependencies
npm install remotion @remotion/cli @remotion/bundler @remotion/captions @remotion/transitions @remotion/install-whisper-cpp react react-dom
npm install -D typescript @types/react

# Setup whisper.cpp for transcription
npx ts-node scripts/setup-whisper.ts
```
