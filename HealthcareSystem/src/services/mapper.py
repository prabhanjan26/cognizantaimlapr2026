import typing
from models.doctor import Doctor
from models.patient import Patient


def map_patient_to_doctor(patient: Patient, doctors: list[Doctor]) -> Doctor | None:
    """
    Maps a patient to a doctor based on disease and specialization.
    """
    if not patient or not doctors:
        return None
    
    for doctor in doctors:
        if doctor.specialization and patient.disease and doctor.specialization.lower() == patient.disease.lower():
            patient.assign_doctor(doctor)
            return doctor
    return None