"""
Person model definition for the healthcare application.
"""
import re
class Person:
    """ A class representing a person with a name and age. """
    def __init__(self, aadharcard: int, mobile_no: int):
        self.__aadharcard = aadharcard
        self.__mobile_no = mobile_no

    @property
    def aadharcard(self):
        """Get the person's aadharcard number."""
        return self.__aadharcard
    
    @property
    def mobile_no(self):
        """Get the person's mobile number."""
        return self.__mobile_no

    @property
    def mobile_no(self):
        """Get the person's mobile number."""
        if not re.match(r'^\d{10}$', str(self.__mobile_no)):
            raise ValueError("Invalid mobile number format. Must be a 10-digit number.")
        return self.__mobile_no