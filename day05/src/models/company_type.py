#create company type class using pydantic
from enum import Enum
class CompanyType(Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"
    NON_PROFIT = "Non-Profit"
