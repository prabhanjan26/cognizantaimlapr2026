from datetime import date
from .transactions import Transaction


class DirectDebit(Transaction):
    """
    Represents a direct debit transaction.

    A DirectDebit is an automatic payment taken from an account
    on a specified payment date.
    """

    def __init__(self, amount: float, sender, receiver, payment_date: date):
        """
        Initializes a DirectDebit transaction.

        :param amount: Amount to be debited
        :param sender: Account paying the debit
        :param receiver: Account receiving the payment
        :param payment_date: Scheduled payment date
        """
        super().__init__(amount, sender, receiver)
        self._payment_date = payment_date

    # ---------- Getter ----------

    def get_payment_date(self) -> date:
        return self._payment_date
