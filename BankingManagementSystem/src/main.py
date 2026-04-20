# from datetime import date

# from menu.menu import Menu
# from customers.individual import Individual
# from customers.corporate import Corporate
# from transactions.transactions import Transaction


# def main():
#     """
#     Entry point of the ABC Banking application.
#     """

#     # ---------- Initialise Menu ----------
#     menu = Menu()

#     # ---------- Create Customers ----------
#     individual_customer = Individual(
#         account_number="IND001",
#         name="John",
#         surname="Doe",
#         gender="Male",
#         date_of_birth=date(1990, 5, 15),
#         address="123 Main Street",
#         contact_number="0712345678",
#         email="john.doe@email.com",
#         password="password123",
#     )

#     corporate_customer = Corporate(
#         account_number="CORP001",
#         name="ABC Solutions",
#         company_type="LTD",
#         address="45 Business Park",
#         contact_number="0711122233",
#         email="contact@abcsolutions.com",
#         password="corpPass",
#     )

#     menu.add_customer(individual_customer)
#     menu.add_customer(corporate_customer)

#     # ---------- Open Accounts ----------
#     savings_account = menu.open_account(
#         "savings",
#         5000.0,
#         date.today(),
#         0.02,
#     )

#     current_account = menu.open_account(
#         "current",
#         2000.0,
#         date.today(),
#         1000.0,
#     )

#     # ---------- Login ----------
#     login_success = menu.login("john.doe@email.com", "password123")
#     print(f"Login successful: {login_success}")

#     # ---------- Perform Transaction ----------
#     transaction = Transaction(
#         amount=500.0,
#         sender=savings_account,
#         receiver=current_account,
#     )

#     menu.initiate_transaction(transaction)

#     # ---------- Display Results ----------
#     print("\n--- Account Balances ---")
#     print(f"Savings Account Balance: {savings_account.get_running_totals()}")
#     print(f"Current Account Balance: {current_account.get_running_totals()}")

#     print("\n--- Savings Account Transactions ---")
#     for txn in savings_account.show_customer_transactions():
#         print(f"Amount: {txn.get_amount()}, Time: {txn.get_time_stamp()}")

#     print("\n--- Current Account Transactions ---")
#     for txn in current_account.show_customer_transactions():
#         print(f"Amount: {txn.get_amount()}, Time: {txn.get_time_stamp()}")

#     # ---------- Logout ----------
#     menu.logout()
#     print("\nUser logged out.")


# if __name__ == "__main__":
#     main()


from menu.menu import Menu

def main():
    menu = Menu()
    menu.run()

if __name__ == "__main__":
    main()