"""
Patient store for managing patient records.
"""
from config.logger_config import setup_logger
from models.patient import Patient
from exceptions.patient_not_found import PatientNotFoundException
 
logger = setup_logger()
 
class PatientStore:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
 
    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        logger.info(f"Patient added: {patient}")
   
 
    def get_patient_by_id(self, patient_id: int) -> Patient:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(patient_id)

    def update_patient(self, patient_id: int, name: str = None, ailment: str = None) -> Patient:
        patient = self.get_patient_by_id(patient_id)
        logger.info(f"Updating patient with id {patient_id}.")
        if name:
            patient.name = name
        if ailment:
            patient.ailment = ailment
        return patient

    def delete_patient(self, patient_id: int):
        logger.info(f"Deleting patient with id {patient_id}.")
        for index, patient in enumerate(self.patients):
            if patient.id == patient_id:
                del self.patients[index]
                return
        raise PatientNotFoundException(patient_id)
 