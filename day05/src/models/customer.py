from pydantic import BaseModel, Field
from .full_name import FullName
class Customer(BaseModel):
    customer_id: int = Field(..., gt=0, description="Customer ID must be a positive integer")
    name: FullName
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', description="Email must be a valid email address")
    phone_no: int = Field(..., gt=1000000000, le=9999999999, description="Phone number must be a positive integer")
