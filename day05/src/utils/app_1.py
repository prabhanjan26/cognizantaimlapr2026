# add project root to python path
import sys
import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_path)

from day05.src.dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from day05.src.stores.customer_store_implement import CustomerStoreImpl
from day05.src.config.conf import Config


def display_customer(customer_store):
    config = Config()
    env = config.app_env

    if env == "production":
        data_loader = CustomerJSONDataLoader()
        data_loader.load_data(
            config.resource_path("customer.json"),
            customer_store
        )

        for customer in customer_store.get_all_customer():
            print(customer)


if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    display_customer(customer_store)