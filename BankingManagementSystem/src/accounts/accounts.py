from abc import ABC, abstractmethod
from datetime import date


class Account(ABC):
    """
    Abstract base class for all account types.
    """

    def __init__(self, opening_balance: float, open_date: date):
        self._running_totals = opening_balance
        self._open_date = open_date
        self._transactions = []

    # ---------- Getters & Setters ----------

    def get_running_totals(self) -> float:
        return self._running_totals

    def set_running_totals(self, amount: float) -> None:
        self._running_totals = amount

    def get_open_date(self) -> date:
        return self._open_date

    def set_open_date(self, open_date: date) -> None:
        self._open_date = open_date

    def get_transactions(self) -> list:
        return self._transactions

    # ---------- Business Logic ----------

    def add_transaction(self, transaction) -> None:
        """
        Adds a transaction to the account's transaction list.
        """
        self._transactions.append(transaction)

    def show_customer_transactions(self) -> list:
        """
        Returns all transactions related to this account.
        """
        return self._transactions

    def can_withdraw(self, amount: float) -> bool:
        """
        Checks whether this account has sufficient funds for the withdrawal.

        Savings accounts cannot go below zero by default.
        """
        return (self._running_totals - amount) >= 0

    # ---------- Abstract Behaviour ----------

    @abstractmethod
    def account_type(self) -> str:
        """
        Must be implemented by subclasses to identify account type.
        """
        pass
