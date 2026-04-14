# creating entry point for the application
import faker 
from store.customer_store import CustomerStore
from view.customer_view import CustomerView
from model.customer import Customer
from datetime import date
"""
This is the main entry point for the application. It initializes the customer store, creates a view, and displays the customers.
"""

def check():
    # Initialize the customer store with 100 customers
    store = CustomerStore(num_customers=100)
    
    # Create a view for the customers
    view = CustomerView(store)
    
    # Display the customers
    view.display_customers()

if __name__ == "__main__":
    check()gti 

