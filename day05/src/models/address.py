#create address class associated to customer using pydantic 
from pydantic import BaseModel, Field
from .customer import Customer
class Address(BaseModel):
    customer: Customer
    street: str = Field(..., description="Street must be a string")
    city: str = Field(..., description="City must be a string")
    state: str = Field(..., description="State must be a string")
    zip_code: str = Field(...,description="Zip code")
    country: str = Field(..., description="Country must be a string")
    