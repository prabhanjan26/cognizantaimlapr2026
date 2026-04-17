""" Create class staff inhertes from person class and associated to role as attribute."""
from models.role import Role

from src.models.person import Person
from src.models.role import Role
class Staff(Person):
    """ class staff 
    """
    def __init__(self, aadharcard: int, mobile_no: int, role: Role):
        super().__init__(aadharcard, mobile_no)
        self.__role = role

    @property
    def role(self):
        """Get the staff's role."""
        return self.__role
    
    @role.setter
    def role(self, value: Role):
        self.__role = value