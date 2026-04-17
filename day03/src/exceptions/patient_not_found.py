"""
Patient not found exception.
"""
class PatientNotFoundException(Exception):
    """Exception raised when a patient is not found."""
    def __init__(self, message="Patient not found."):
        self.message = message
        super().__init__(self.message)
        