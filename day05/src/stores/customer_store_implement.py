#create customer store implementation class that inherits from customer store abstract class
from day05.src.exceptions.customer_not_found import CustomerNotFound

from .customer_store import CustomerStore
from ..exceptions.customer_not_found import CustomerNotFound
class CustomerStoreImpl(CustomerStore):
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
    
    def get_all_customer(self):
        return self.customers
    
    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        raise CustomerNotFound(customer_id)

    def update_customer(self, customer_id, customer):
        for i, c in enumerate(self.customers):
            if c.customer_id == customer_id:
                self.customers[i] = customer
                return
        raise CustomerNotFound(customer_id)

    def delete_customer(self, customer_id):
        for i in range(len(self.customers)):
            if self.customers[i].customer_id == customer_id:
                del self.customers[i]
                return