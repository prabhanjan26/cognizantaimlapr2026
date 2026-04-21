import pandas as pd
from day05.src.dataloaders.customer_data_loaders import CustomerDataLoader
from day05.src.stores.customer_store_implement import CustomerStoreImpl
from day05.src.models.full_name import FullName
from day05.src.models.customer import Customer
class CustomerCSVDataLoader(CustomerDataLoader):
    def load_data(self, file_name, customer_stores: CustomerStoreImpl):
        df = pd.read_csv(file_name)
        for _, row in df.iterrows():
            customer_id = int(row['customer_id'])
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_no = row['phone_no']
            customer = Customer(
                customer_id=customer_id,
                name=FullName(first_name=first_name, last_name=last_name),
                email=email,
                phone_no=phone_no
            )
            customer_stores.add_customer(customer)
