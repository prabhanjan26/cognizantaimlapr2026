"""
Doctor Not Found Exception
"""
class DoctorNotFoundException(Exception):
    """Exception raised when a doctor is not found."""
    def __init__(self, message="Doctor not found."):
        self.message = message
        super().__init__(self.message)