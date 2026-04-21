#create configuration for the file 
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    app_env: str = os.getenv("APP_ENV", "development")

    def resource_path(self, resource_name: str) -> str:
        if self.app_env == "Production":
            return f"src/resources/customer.json"
        elif self.app_env == "Testing":
            return f"src/resources/customer.txt"
        elif self.app_env == "development" or self.app_env == "Development":
            return f"src/resources/customer.csv" #Default to CSV for development environment
        else:
            raise ValueError(f"Invalid APP_ENV value")
        
        
