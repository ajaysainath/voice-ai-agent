import os
import time
from fastapi import WebSocket
from services.speech_to_text import transcribe_audio
from agent.agent_controller import understand_request
from scheduler.appointment_engine import check_availability, book_appointment
from services.text_to_speech import speak_text

from starlette.websockets import WebSocketDisconnect

# get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        try:
            start = time.time()

            data = await websocket.receive_text()
            audio_file = os.path.join(BASE_DIR, data)

            stt_start = time.time()
            user_text = transcribe_audio(audio_file)
            stt_time = time.time() - stt_start

            agent_start = time.time()
            intent_data = understand_request(user_text)
            agent_time = time.time() - agent_start

            intent = intent_data["intent"]
            doctor = intent_data["doctor"]
            date = intent_data["date"]

            if intent == "book":
                slots = check_availability(doctor)
                if slots:
                    response = book_appointment(doctor, date, slots[0])
                else:
                    response = "No slots available"
            else:
                response = "I could not understand the request"

            tts_start = time.time()
            speak_text(response)
            tts_time = time.time() - tts_start

            total_time = time.time() - start

            print("STT latency:", stt_time)
            print("Agent latency:", agent_time)
            print("TTS latency:", tts_time)
            print("Total latency:", total_time)

            await websocket.send_text(response)

        except WebSocketDisconnect:
            print("Client disconnected")
            break

        except Exception as e:
            print("Error:", e)
            break