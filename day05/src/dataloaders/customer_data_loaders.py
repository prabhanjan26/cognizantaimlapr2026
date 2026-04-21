#create customer data loader abstract class 
from abc import ABC, abstractmethod
from day05.src.stores.customer_store_implement import CustomerStoreImpl
from day05.src.exceptions.customer_not_found import CustomerNotFound
class CustomerDataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        pass