from scheduler.appointment_engine import check_availability, book_appointment

doctor = "cardiologist"
date = "tomorrow"

slots = check_availability(doctor)

print("Available slots:", slots)

if slots:
    confirmation = book_appointment(doctor, date, slots[0])
    print(confirmation)