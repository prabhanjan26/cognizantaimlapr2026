"""
Create appointment

"""
from datetime import date, time
from models.doctor import Doctor
from models.patient import Patient

class Appointment:
    def __init__(self, id: int, date: date, time: time, doctor : Doctor, patient : Patient):
        self.id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient

    def __str__(self):
        return f"Appointment {self.id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time}"