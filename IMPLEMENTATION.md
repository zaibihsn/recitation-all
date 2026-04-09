# Implementation Guide

This guide explains how the audio files and word-by-word timestamp data are structured in this repository, and provides implementation examples to help you build a seamless playback and highlighting experience across various major technology stacks.

## 🗂️ Data Structure

The repository uses a highly structured directory format to make programmatic access to any verse's audio and timing data incredibly simple.

### Directory Layout
Files are organized in the following hierarchy:
`/{reciter_name}/{surah_index}/{surah_index}{verse_index}.[opus|json]`

Where:
- `{reciter_name}`: The slugged directory name of the reciter (e.g., `abdul-basit-abdul-samad-murattal-hafs-950`).
- `{surah_index}`: The Surah number, strictly 3-digit zero-padded (e.g., `001` for Al-Fatihah, `114` for An-Nas).
- `{verse_index}`: The Verse number, strictly 3-digit zero-padded. Combined, `{surah_index}{verse_index}` creates a 6-digit filename prefix (e.g., `001001` or `114006`).

**Example Paths**:
- 🎵 **Audio**: `https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all@main/abdul-basit-abdul-samad-murattal-hafs-950/001/001001.opus`
- ⏱️ **Metadata**: `https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all@main/abdul-basit-abdul-samad-murattal-hafs-950/001/001001.json`

### JSON Metadata Formats
When fetching the `.json` files, you will encounter one of two primary formats depending on the data source. Your parsing logic should seamlessly handle both.

**Format A (Flat Array)**
A direct array of timestamps. Each inner array element represents a specific word.
```json
[
  [0, 1, 0, 920], 
  [1, 2, 1080, 1440], 
  [2, 3, 2120, 2440]
]
```
*Structure: `[current_word_index, next_word_index, start_time_ms, end_time_ms]`*

**Format B (Detailed Object)**
An object containing verse metadata along with an array of word segments.
```json
{
  "verse_key": "1:1",
  "timestamp_from": 0,
  "timestamp_to": 8037,
  "segments": [
    [1, 0, 579], 
    [2, 579, 1331]
  ]
}
```
*Structure within `segments`: `[word_index, start_time_ms, end_time_ms]`*

---

## 💻 Tech Stack Implementations

The core concept across all frameworks is:
1. Fetch the JSON timestamp array for a verse.
2. Load the Audio track for that verse.
3. Listen to the audio stream's current position (time).
4. Given the current time in milliseconds, loop over the timestamps and find the word where `start_time <= current_time <= end_time`.
5. Apply a "highlighted" style/class to that word index.

### 1. Vanilla JavaScript
```javascript
const audio = new Audio("https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all@main/abdul-basit.../001/001001.opus");
let timestamps = []; // E.g., [[0,1,0,920], [1,2,1080,1440]]
let activeWordIndex = -1;

audio.addEventListener("timeupdate", () => {
    const currentTimeMs = audio.currentTime * 1000;
    
    // Find matching word
    const match = timestamps.find(t => {
        // Handle both format variants appropriately (Format A in this example)
        return currentTimeMs >= t[2] && currentTimeMs <= t[3];
    });

    if (match) {
        const newWordIndex = match[0];
        if (activeWordIndex !== newWordIndex) {
            activeWordIndex = newWordIndex;
            highlightWordInDOM(activeWordIndex); // Your custom function
        }
    }
});

audio.play();
```

### 2. React.js
```tsx
import React, { useState, useEffect, useRef } from 'react';

const QuranPlayer = ({ audioUrl, timestamps, words }) => {
  const audioRef = useRef(null);
  const [activeWordIndex, setActiveWordIndex] = useState(-1);

  const handleTimeUpdate = () => {
    if (!audioRef.current || !timestamps) return;
    
    const currentTimeMs = audioRef.current.currentTime * 1000;
    
    // Assume Format A timestamps: [wordIdx, nextIdx, startMs, endMs]
    const match = timestamps.find(
      (t) => currentTimeMs >= t[2] && currentTimeMs <= t[3]
    );

    if (match && match[0] !== activeWordIndex) {
      setActiveWordIndex(match[0]);
    } else if (!match && activeWordIndex !== -1) {
      setActiveWordIndex(-1); // Resets when pause/delay happens
    }
  };

  return (
    <div>
      <audio ref={audioRef} src={audioUrl} onTimeUpdate={handleTimeUpdate} controls />
      <div className="quran-text">
        {words.map((word, index) => (
          <span key={index} className={index === activeWordIndex ? "text-blue-500 font-bold" : "text-black"}>
            {word}
          </span>
        ))}
      </div>
    </div>
  );
};
```

### 3. Vue 3 (Composition API)
```vue
<script setup>
import { ref, onMounted } from 'vue';

const audioUrl = ref("https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all@main/...opus");
const activeWordIndex = ref(-1);
// Assuming array of Format A timestamps loaded here
const timestamps = ref([[0, 1, 0, 920], [1, 2, 1080, 1440]]);
const words = ref(["Bismillah", "ir-Rahman", "ir-Raheem"]); 

const onTimeUpdate = (event) => {
  const currentTimeMs = event.target.currentTime * 1000;
  
  const match = timestamps.value.find(t => currentTimeMs >= t[2] && currentTimeMs <= t[3]);
  activeWordIndex.value = match ? match[0] : -1;
};
</script>

<template>
  <div>
    <audio :src="audioUrl" @timeupdate="onTimeUpdate" controls />
    <p>
      <span 
        v-for="(word, i) in words" 
        :key="i"
        :class="{ 'highlighted-word': i === activeWordIndex }"
      >
        {{ word }}
      </span>
    </p>
  </div>
</template>

<style scoped>
.highlighted-word { color: #3b82f6; font-weight: bold; }
</style>
```

### 4. Flutter (Dart)
Using the popular `just_audio` package.

```dart
import 'package:flutter/material.dart';
import 'package:just_audio/just_audio.dart';

class QuranPlayerWidget extends StatefulWidget {
  final String audioUrl;
  final List<dynamic> timestamps;  // Parsed JSON
  final List<String> words; 

  QuranPlayerWidget({required this.audioUrl, required this.timestamps, required this.words});

  @override
  _QuranPlayerWidgetState createState() => _QuranPlayerWidgetState();
}

class _QuranPlayerWidgetState extends State<QuranPlayerWidget> {
  final AudioPlayer _player = AudioPlayer();
  int _activeWordIndex = -1;

  @override
  void initState() {
    super.initState();
    _initPlayer();
  }

  Future<void> _initPlayer() async {
    await _player.setUrl(widget.audioUrl);
    
    _player.positionStream.listen((position) {
      final currentTimeMs = position.inMilliseconds;
      int matchIndex = -1;

      for (var t in widget.timestamps) {
        // Format A check: [wordIndex, nextIndex, start, end]
        if (currentTimeMs >= t[2] && currentTimeMs <= t[3]) {
          matchIndex = t[0];
          break;
        }
      }

      if (_activeWordIndex != matchIndex) {
        setState(() {
          _activeWordIndex = matchIndex;
        });
      }
    });
  }

  @override
  void dispose() {
    _player.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Wrap(
      children: widget.words.asMap().entries.map((entry) {
        bool isActive = entry.key == _activeWordIndex;
        return Text(
          entry.value + " ",
          style: TextStyle(
            color: isActive ? Colors.blue : Colors.black,
            fontWeight: isActive ? FontWeight.bold : FontWeight.normal,
          ),
        );
      }).toList(),
    );
  }
}
```

---

## 🤖 AI Prompt Generator 

If you are using ChatGPT, Claude, GitHub Copilot, or Cursor to build your application, you can copy and paste the prompt below to get an instant, perfectly structured word-by-word active highlighting system tailored to this repository's structure.

> **Copy this Prompt:**
> 
> "I am building a Quran application where I need to play audio for a Quran verse and highlight the textual Arabic words as they are being spoken (karaoke style). 
> 
> The verse audio is hosted via CDN: `https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all@main/{reciter_name}/{surah_padded}/{surah_padded}{verse_padded}.opus`. (E.g., Surah 1 Verse 1 for reciter 'abdul-basit-abdul-samad-murattal-hafs-950' is `.../001/001001.opus`).
> 
> The timestamp file is located at the exact same path but with a `.json` extension instead (e.g. `.../001/001001.json`). 
> The timestamp JSON could come in one of two formats:
> 1. A flat array of arrays: `[[word_index, next_word_index, start_time_ms, end_time_ms]]`.
> 2. A detailed object: `{"segments": [[word_index, start_time_ms, end_time_ms]]}`.
>
> Please write the UI and logic using **[INSERT YOUR STACK/FRAMEWORK HERE]**.
> Requirements:
> 1. Fetch and parse both timestamp formats safely.
> 2. Initialize an audio player streaming the `.opus` file.
> 3. Track the current playback time of the audio stream in milliseconds.
> 4. Use the timestamp interval logic (`start_time <= current_time <= end_time`) to determine the active active word index.
> 5. Map over a list of placeholder strings (simulating Arabic words) and visually highlight the word that corresponds to the active word index."
