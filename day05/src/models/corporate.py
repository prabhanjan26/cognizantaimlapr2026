#create corporate class inherit from customer using pydantic
from pydantic import Field
from .customer import Customer
from .company_type import CompanyType
class Corporate(Customer):
    reg_no: str = Field(..., description="Company registration number must be a string")
    company_type: CompanyType