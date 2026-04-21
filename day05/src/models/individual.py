#create class individual using pydantic
from pydantic import Field, FieldValidator
from .customer import Customer
from .gender import Gender
from datetime import date

class Individual(Customer):
    gender: Gender 
    dob: date = Field(..., description="Date of Birth must be a valid date in the format YYYY-MM-DD")

    @FieldValidator('dob')
    def validate_dob(cls, v):
        if v > date.today():
            raise ValueError("Date of Birth must be in the past")
        age = (date.today() - v).days // 365
        if age < 18:
            raise ValueError("Individual must be at least 18 years old")
        return v
