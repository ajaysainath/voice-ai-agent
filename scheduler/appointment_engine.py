doctor_schedule = {
    "cardiologist": ["10:00 AM", "12:00 PM", "3:00 PM"],
    "dermatologist": ["11:00 AM", "2:00 PM"]
}

booked_appointments = []


def check_availability(doctor):
    return doctor_schedule.get(doctor, [])


def book_appointment(doctor, date, time):

    appointment = {
        "doctor": doctor,
        "date": date,
        "time": time
    }

    if appointment in booked_appointments:
        return "Slot already booked."

    booked_appointments.append(appointment)

    return f"Appointment booked with {doctor} on {date} at {time}"