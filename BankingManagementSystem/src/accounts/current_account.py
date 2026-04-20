from datetime import date
from .accounts import Account


class CurrentAccount(Account):
    """
    Represents a current account.

    A CurrentAccount allows overdraft up to a specified limit.
    It inherits common account functionality from the Account class
    and adds overdraft-specific behaviour.
    """

    def __init__(self, opening_balance: float, open_date: date, overdraft_limit: float):
        """
        Initializes a CurrentAccount object.

        :param opening_balance: Initial balance when the account is opened
        :param open_date: Date the account was opened
        :param overdraft_limit: Maximum overdraft allowed
        """
        super().__init__(opening_balance, open_date)
        self._overdraft_limit = overdraft_limit

    # ---------- Getters & Setters ----------

    def get_overdraft_limit(self) -> float:
        return self._overdraft_limit

    def set_overdraft_limit(self, overdraft_limit: float) -> None:
        self._overdraft_limit = overdraft_limit

    # ---------- Business Logic ----------

    def can_withdraw(self, amount: float) -> bool:
        """
        Checks whether a withdrawal can be made without exceeding
        the overdraft limit.

        :param amount: Amount to withdraw
        :return: True if withdrawal is allowed, False otherwise
        """
        return (self._running_totals - amount) >= -self._overdraft_limit

    # ---------- Abstract Method Implementation ----------

    def account_type(self) -> str:
        """
        Returns the type of the account.
        """
        return "Current Account"