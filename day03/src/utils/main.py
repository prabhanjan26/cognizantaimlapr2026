"""
main file to run the person model tests. and access the person data like mobile number and aadhar card number.
"""
import logging
from venv import logger

# Create a person instance

import faker
from models.person import Person
from models.staff import Staff
setup_logger = logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def create_person(aadharcard: int, mobile_no: int):
    person = Person(aadharcard = '1234-5678-9012', mobile_no = 9876543210)
    print(f"Aadhar Card: {person.aadharcard}")
    print(f"Mobile Number: {person.mobile_no}")

    """Update mobile number with valid format"""
    try:
        person.mobile_no = faker.random_number(digits=6)  # Valid mobile number
        logger.info(f"Updated Mobile Number: {person.mobile_no}")
    except ValueError as e: 
        logger.error(e)



# p1 = Person(123456789012, 9876543210)

# # Access the person's data
# print(p1.aadharcard)
# print(p1.mobile_no)
def create_staff(aadharcard: int, mobile_no: int, role):
    role = role(name='manager', descrip)
    
    staff = Staff(aadharcard = '1234-5678-9012', mobile_no = 9876543210, role = role)
    print(f"Aadhar Card: {staff.aadharcard}, Mobile Number: {staff.mobile_no}, Role: {staff.role}")