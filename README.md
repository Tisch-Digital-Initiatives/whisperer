# whisperer
Simple Python script to run whisper transcription on audio or video files.

## Requirements
- Python3
- openai-whisper
- pathlib
- ffmpeg

## Installation
Install whisper, pathlib, and ffmpeg:
```
pip install -U openai-whisper
```
```
pip install -U pathlib
```
```
pip install -U ffmpeg
```

## Usage
- Choose and input a whisper model.
- Input the full filepath for your audio or video file
- Upon completion, .srv, .tsv, and .txt transcripts will be saved in output/ subdirectory with the same filename as the input

