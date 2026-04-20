from .transactions import Transaction


class ExternalTransaction(Transaction):
    """
    Represents an external transaction.

    An ExternalTransaction records a transfer involving
    another bank or branch outside the main banking group.
    """

    def __init__(
        self,
        amount: float,
        sender,
        receiver,
        branch_name: str,
        branch_address: str,
        branch_post_code: str,
        branch_code: str,
    ):
        """
        Initializes an ExternalTransaction.

        :param amount: Amount transferred
        :param sender: Sending account
        :param receiver: Receiving account
        :param branch_name: Name of the external branch
        :param branch_address: Address of the external branch
        :param branch_post_code: Branch postcode
        :param branch_code: Branch identifying code
        """
        super().__init__(amount, sender, receiver)
        self._branch_name = branch_name
        self._branch_address = branch_address
        self._branch_post_code = branch_post_code
        self._branch_code = branch_code

    # ---------- Getters ----------

    def get_branch_name(self) -> str:
        return self._branch_name

    def get_branch_address(self) -> str:
        return self._branch_address

    def get_branch_post_code(self) -> str:
        return self._branch_post_code

    def get_branch_code(self) -> str:
        return self._branch_code