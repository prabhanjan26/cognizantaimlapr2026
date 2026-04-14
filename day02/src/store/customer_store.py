#generate 100 customers
from faker import Faker
from model.customer import Customer
import typing
class CustomerStore:
    def __init__(self, num_customers: int = 100):
        self.customers = self._generate_customers(num_customers)

    def _generate_customers(self, num_customers: int) -> typing.List[Customer]:
        fake = Faker()
        customers = []
        for _ in range(num_customers):
            name = fake.name()
            email = fake.email()
            dob = fake.date_of_birth()
            customers.append(Customer(name, email, dob))
        return customers

    def get_all_customers(self) -> typing.List[Customer]:
        return self.customers