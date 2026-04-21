#create the customer txt data loader class that inherits from customer data loader abstract class.
import pandas as pd
from day05.src.dataloaders.customer_data_loaders import CustomerDataLoader
from day05.src.stores.customer_store_implement import CustomerStoreImpl
from day05.src.models.full_name import FullName
from day05.src.models.customer import Customer
class CustomerTXTDataLoader(CustomerDataLoader):
    def load_data(self, file_name, customer_stores: CustomerStoreImpl):
        with open(file_name, 'r') as file:
            customer_data = {}
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    if customer_data:
                        # Create customer from collected data
                        customer = Customer(
                            customer_id=customer_data['customer_id'],
                            name=FullName(
                                first_name=customer_data['first_name'],
                                last_name=customer_data['last_name']
                            ),
                            email=customer_data['email'],
                            phone_no=customer_data['phone_no']
                        )
                        customer_stores.add_customer(customer)
                        customer_data = {}
                else:
                    # Parse key-value pair
                    key, value = line.split(': ')
                    if key == 'customer_id':
                        customer_data['customer_id'] = int(value)
                    else:
                        customer_data[key] = value
            
            # Handle last customer if file doesn't end with blank line
            if customer_data:
                customer = Customer(
                    customer_id=customer_data['customer_id'],
                    name=FullName(
                        first_name=customer_data['first_name'],
                        last_name=customer_data['last_name']
                    ),
                    email=customer_data['email'],
                    phone_no=customer_data['phone_no']
                )
                customer_stores.add_customer(customer)