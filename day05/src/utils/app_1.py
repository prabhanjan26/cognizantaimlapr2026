# add project root to python path
import sys
import os
from src.exceptions.customer_not_found import CustomerNotFound
from faker import Faker


project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_path)

from src.dataloaders.customer_txt_dataloader import CustomerTXTDataLoader
from src.dataloaders.customer_csv_dataloader import CustomerCSVDataLoader
from src.dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from src.stores.customer_store_implement import CustomerStoreImpl
from src.config.conf import Config
from src.utils.pipeline_runner import PipeLineRunner

def load_customer_data(**kwargs):
    config = Config()
    env = config.app_env
    customer_store = kwargs.get('customer_store')

    if env == "production":
        data_loader = CustomerJSONDataLoader()
        data_loader.load_data(
            config.resource_path("customer.json"),
            customer_store
        )
    if env == "development":
        data_loader = CustomerCSVDataLoader() ## csv
        data_loader.load_data(
            config.resource_path("customer.csv"),
            customer_store
        )
    if env == "testing":
        data_loader = CustomerTXTDataLoader() ## txt
        data_loader.load_data(
            config.resource_path("customer.txt"),
            customer_store
        )
    return customer_store

def update_customer_data(**kwargs):
    customer_store = kwargs.get('customer_store')
    customer_id = kwargs.get('customer_id')
    customer = customer_store.get_customer(customer_id)
    fake = Faker()
    if customer:
        customer.name.first_name = fake.first_name()
        customer.name.last_name = fake.last_name()
        customer.email = fake.email()
        customer.phone_no = fake.phone_number()
        print(f"Customer with ID {customer_id} has been updated.")
    else:
        print(f"Customer with ID {customer_id} not found.")

def get_customer_by_id(**kwargs):
    customer_store = kwargs.get('customer_store')
    customer_id = kwargs.get('customer_id', None)
    customer = customer_store.get_customer(customer_id)
    try:
        customer = customer_store.get_customer(customer_id)
        print(f"Customer ID: {customer.customer_id}")
        print(f"Name: {customer.name.first_name} {customer.name.last_name}")
        print(f"Email: {customer.email}")
        print(f"Phone No: {customer.phone_no}")
        print(f"Successfully retrieved customer with ID {customer_id}.")
    except CustomerNotFound as e:
        print(e)

def delete_customer_by_id(**kwargs):
    customer_store = kwargs.get('customer_store')
    customer_id = kwargs.get('customer_id', None)
    try:
        customer_store.delete_customer(customer_id)
        print(f"Customer with ID {customer_id} has been deleted.")
    except CustomerNotFound as e:
        print(e)

def display_customer(**kwargs):
    customer_store = kwargs.get('customer_store')
    customer_id = kwargs.get('customer_id', None)
    customers = customer_store.get_all_customers()
    for customer in customers:
        print(f"Customer ID: {customer.customer_id}")
        print(f"Name: {customer.name.first_name} {customer.name.last_name}")
        print(f"Email: {customer.email}")
        print(f"Phone No: {customer.phone_no}")
        print("--------------------------------------------------")

        


if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    pipline_runner = PipeLineRunner()
    pipline_runner.add_stage(load_customer_data)
    pipline_runner.add_stage(display_customer)
    pipline_runner.add_stage(update_customer_data)
    pipline_runner.add_stage(get_customer_by_id)
    pipline_runner.add_stage(delete_customer_by_id)

    pipline_runner.run(customer_store=customer_store, customer_id=1)