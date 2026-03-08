from gtts import gTTS

def speak_text(text):

    tts = gTTS(text=text, lang="en")

    output_file = "response_audio.mp3"

    tts.save(output_file)

    print("Audio response saved as:", output_file)