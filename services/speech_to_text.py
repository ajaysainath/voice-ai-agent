import whisper
import os

# Tell Python exactly where ffmpeg is
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-8.0.1-essentials_build\bin"

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]