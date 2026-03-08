import re

def understand_request(user_text):

    text = user_text.lower()

    intent = None
    doctor = None
    date = None

    if "book" in text or "appointment" in text:
        intent = "book"

    if "cancel" in text:
        intent = "cancel"

    if "reschedule" in text or "move" in text:
        intent = "reschedule"

    if "cardiologist" in text:
        doctor = "cardiologist"

    if "dermatologist" in text:
        doctor = "dermatologist"

    if "tomorrow" in text:
        date = "tomorrow"

    if "today" in text:
        date = "today"

    return {
        "intent": intent,
        "doctor": doctor,
        "date": date
    }