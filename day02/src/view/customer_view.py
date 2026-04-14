#view customer details
from store.customer_store import CustomerStore
class CustomerView:
    def __init__(self, store: CustomerStore):
        self.store = store

    def display_customers(self):
        customers = self.store.get_all_customers()
        for customer in customers:
            print(customer)