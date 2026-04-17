## define a doctor class
class Doctor:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Dr. {self.id}, {self.name}, {self.specialty}"