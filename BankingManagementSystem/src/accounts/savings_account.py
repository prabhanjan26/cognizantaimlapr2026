from datetime import date
from .accounts import Account


class SavingsAccount(Account):
    """
    Represents a savings account.

    A SavingsAccount earns interest on the available balance.
    It inherits common account behaviour from the Account class
    and adds an interest rate attribute.
    """

    def __init__(self, opening_balance: float, open_date: date, interest_rate: float):
        """
        Initializes a SavingsAccount object.

        :param opening_balance: Initial balance when the account is opened
        :param open_date: Date the account was opened
        :param interest_rate: Annual interest rate applied to the balance
        """
        super().__init__(opening_balance, open_date)
        self._interest_rate = interest_rate

    # ---------- Getters & Setters ----------

    def get_interest_rate(self) -> float:
        return self._interest_rate

    def set_interest_rate(self, interest_rate: float) -> None:
        self._interest_rate = interest_rate

    # ---------- Business Logic ----------

    def apply_interest(self) -> None:
        """
        Applies interest to the current account balance.
        """
        interest_amount = self._running_totals * self._interest_rate
        self._running_totals += interest_amount

    # ---------- Abstract Method Implementation ----------

    def account_type(self) -> str:
        """
        Returns the type of the account.
        """
        return "Savings Account"