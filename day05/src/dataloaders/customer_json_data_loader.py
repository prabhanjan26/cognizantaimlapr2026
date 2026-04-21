import json
from day05.src.dataloaders.customer_data_loaders import CustomerDataLoader
from day05.src.stores.customer_store_implement import CustomerStoreImpl
from day05.src.models.full_name import FullName
from day05.src.models.customer import Customer


class CustomerJSONDataLoader(CustomerDataLoader):
    def load_data(self, file_name: str, customer_stores: CustomerStoreImpl):
        with open(file_name, 'r') as file:
            data = json.load(file)

            for item in data:
                customer_id = int(item['customer_id'])
                first_name = item['name']['first_name']
                last_name = item['name']['last_name']
                email = item['email']
                phone_no = item['phone_no']

                customer = Customer(
                    customer_id=customer_id,
                    name=FullName(first_name=first_name, last_name=last_name),
                    email=email,
                    phone_no=phone_no
                )

                customer_stores.add_customer(customer)