import typing 
class Patient:
    """
    Represents a patient with a disease.
    """

    def __init__(self, name: str, disease: str):
        self.name = name
        self.disease = disease
        self.assigned_doctor = None

    def assign_doctor(self, doctor):
        self.assigned_doctor = doctor

    def __repr__(self):
        return (
            f"Patient(name={self.name}, disease={self.disease}, "
            f"doctor={self.assigned_doctor.name if self.assigned_doctor else 'None'})"
        )