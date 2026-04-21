import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from datetime import date
from typing import Optional, Union

from accounts.savings_account import SavingsAccount
from accounts.current_account import CurrentAccount
from customers.individual import Individual
from customers.corporate import Corporate
from transactions.transactions import Transaction
from bank.sbi_bank import StateBankOfIndia


class Menu:
    """
    Acts as the main controller of the banking system.
    Provides a CLI interface for user interaction.
    """

    def __init__(self):
        self._customer_list = []
        self._customer_account_list = []
        self._transaction_list = []

        self._bank = StateBankOfIndia("SBI Banking Group")
        self._current_user: Optional[Union[Individual, Corporate]] = None

    # ======================
    # CLI ENTRY POINT
    # ======================

    def run(self):
        """Starts the CLI loop."""
        while True:
            print("\n=== ABI Banking System ===")
            print("1. Register Customer")
            print("2. Login")
            print("3. Exit")

            choice = input("Select an option: ").strip()

            if choice == "1":
                self._register_customer()
            elif choice == "2":
                self._login_flow()
            elif choice == "3":
                print("Logged out.")
                break
            else:
                print("Invalid option.")

    # ======================
    # AUTH FLOWS
    # ======================

    def _login_flow(self):
        email = input("Email: ").strip()
        password = input("Password: ").strip()

        if self.login(email, password):
            print("Login successful.")
            self._logged_in_menu()
        else:
            print("Invalid credentials.")

    def _register_customer(self):
        print("\n--- Register Customer ---")
        print("1. Individual")
        print("2. Corporate")

        customer_type = input("Select customer type: ").strip()

        if customer_type == "1":
            self._register_individual()
        elif customer_type == "2":
            self._register_corporate()
        else:
            print("Invalid customer type.")

    def _logged_in_menu(self):
        while True:
            print("\n--- Customer Menu ---")
            print("1. Open Savings Account")
            print("2. View Accounts")
            print("3. Make Transaction")
            print("4. Logout")

            choice = input("Select an option: ").strip()

            if choice == "1":
                self._open_savings_account_cli()
            elif choice == "2":
                self._view_accounts()
            elif choice == "3":
                self._make_transaction_cli()
            elif choice == "4":
                self.logout()
                print("Logged out.")
                break
            else:
                print("Invalid option.")

    # ======================
    # CUSTOMER CREATION
    # ======================

    def _register_individual(self):
        print("\n--- Register Individual ---")
        
        name = input("First name: ")
        surname = input("Surname: ")
        gender = input("Gender: ")
        dob = date.fromisoformat(input("Date of birth (YYYY-MM-DD): "))
        address = input("Address: ")
        contact = input("Contact number: ")
        email = input("Email: ")
        password = input("Password: ")
        account_number = input("Account number: ")

        customer = Individual(
            account_number,
            name,
            surname,
            gender,
            dob,
            address,
            contact,
            email,
            password,
        )

        self.add_customer(customer)
        print("Individual registered successfully.")

    def _register_corporate(self):
        print("\n--- Register Corporate ---")
        
        name = input("Company name: ")
        company_type = input("Company type (e.g. LTD, PLC): ")
        address = input("Address: ")
        contact = input("Contact number: ")
        email = input("Email: ")
        password = input("Password: ")
        account_number = input("Account number: ")

        customer = Corporate(
            account_number,
            name,
            company_type,
            address,
            contact,
            email,
            password,
        )

        self.add_customer(customer)
        print("Corporate registered successfully.")

    # ======================
    # ACCOUNT OPERATIONS
    # ======================

    def _open_savings_account_cli(self):
        balance = float(input("Opening balance: "))
        interest = float(input("Interest rate (e.g. 0.02): "))

        account = self.open_account(
            "savings",
            balance,
            date.today(),
            interest,
        )

        print("Savings account opened successfully.")

    def _view_accounts(self):
        print("\n--- Accounts ---")
        if not self._customer_account_list:
            print("No accounts available. Open an account first.")
            return

        for i, acc in enumerate(self._customer_account_list, start=1):
            print(f"{i}. {acc.account_type()} - Balance: {acc.get_running_totals()}")

    # ======================
    # TRANSACTIONS
    # ======================

    def _make_transaction_cli(self):
        if len(self._customer_account_list) < 2:
            print("At least two accounts required. Open another account before transferring.")
            return

        self._view_accounts()

        sender_index = int(input("Select sender account number: ").strip()) - 1
        receiver_index = int(input("Select receiver account number: ").strip()) - 1
        amount = float(input("Amount to transfer: ").strip())

        sender = self._customer_account_list[sender_index]
        receiver = self._customer_account_list[receiver_index]

        try:
            transaction = Transaction(amount, sender, receiver)
            self.initiate_transaction(transaction)
            print("Transaction completed.")
        except ValueError as exc:
            print(f"Transaction failed: {exc}")

    # ======================
    # EXISTING METHODS
    # ======================

    def login(self, email: str, password: str) -> bool:
        for customer in self._customer_list:
            if customer.get_email() == email and customer.get_password() == password:
                self._current_user = customer
                return True
        return False

    def logout(self):
        self._current_user = None

    def add_customer(self, customer):
        self._customer_list.append(customer)

    def open_account(self, account_type: str, *args):
        if account_type == "savings":
            account = SavingsAccount(*args)
        else:
            account = CurrentAccount(*args)

        self._customer_account_list.append(account)
        self._bank.add_account(account)
        return account

    def initiate_transaction(self, transaction: Transaction):
        transaction.withdraw_money()
        transaction.deposit_money()
        self._transaction_list.append(transaction)
