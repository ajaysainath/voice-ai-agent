from memory.session_memory import save_session, get_session

session_id = "patient_1"

data = {
    "intent": "book",
    "doctor": "cardiologist"
}

save_session(session_id, data)

print("Stored session:", get_session(session_id))