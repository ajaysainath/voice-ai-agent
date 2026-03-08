from services.text_to_speech import speak_text
from services.speech_to_text import transcribe_audio
from agent.agent_controller import understand_request
from scheduler.appointment_engine import check_availability, book_appointment

# Step 1: convert voice to text
audio_file = "sample_agent.m4a"
user_text = transcribe_audio(audio_file)

print("User said:", user_text)

# Step 2: understand user request
intent_data = understand_request(user_text)

print("Agent understanding:", intent_data)

intent = intent_data["intent"]
doctor = intent_data["doctor"]
date = intent_data["date"]

# Step 3: scheduling logic
if intent == "book":

    slots = check_availability(doctor)

    print("Available slots:", slots)

    if slots:
        confirmation = book_appointment(doctor, date, slots[0])
        print("System response:", confirmation)

        # convert response to voice
        speak_text(confirmation)

    else:
        response = "No slots available."
        print("System response:", response)
        speak_text(response)