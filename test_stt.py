from services.speech_to_text import transcribe_audio

audio_file = "sample_agent.m4a"

text = transcribe_audio(audio_file)

print("Transcribed Text:", text)