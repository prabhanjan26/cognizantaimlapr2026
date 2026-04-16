import typing 

class Doctor:
    """
    Represents a doctor in the healthcare system.
    """

    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return f"Doctor(name={self.name}, specialization={self.specialization})"