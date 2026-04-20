from abc import ABC
from datetime import datetime


class Transaction(ABC):
    """
    Abstract base class representing a financial transaction.

    A transaction records the movement of money between two accounts.
    This class provides shared attributes and core behaviours that
    all transaction types inherit.
    """

    def __init__(self, amount: float, sender, receiver):
        """
        Initializes a Transaction object.

        :param amount: Amount of money involved in the transaction
        :param sender: Account sending the money
        :param receiver: Account receiving the money
        """
        self._amount = amount
        self._sender = sender
        self._receiver = receiver
        self._time_stamp = datetime.now()

    # ---------- Getters ----------

    def get_amount(self) -> float:
        return self._amount

    def get_sender(self):
        return self._sender

    def get_receiver(self):
        return self._receiver

    def get_time_stamp(self) -> datetime:
        return self._time_stamp

    # ---------- Core Transaction Logic ----------

    def deposit_money(self) -> None:
        """
        Deposits money into the receiver's account
        and records the transaction.
        """
        self._receiver.set_running_totals(
            self._receiver.get_running_totals() + self._amount
        )
        self._receiver.add_transaction(self)

    def withdraw_money(self) -> None:
        """
        Withdraws money from the sender's account
        and records the transaction.
        """
        self._sender.set_running_totals(
            self._sender.get_running_totals() - self._amount
        )
        self._sender.add_transaction(self)
