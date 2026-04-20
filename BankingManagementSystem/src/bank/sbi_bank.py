class StateBankOfIndia:
    """
    Represents the State Bank of India (SBI).

    The StateBankOfIndia aggregates multiple bank accounts.
    It provides functionality to manage accounts but does
    not control their lifecycle or transactional behaviour.
    """

    def __init__(self, bank_name: str):
        """
        Initializes the banking group.

        :param bank_name: Name of the banking group
        """
        self._bank_name = bank_name
        self._accounts = []

    # ---------- Getters ----------

    def get_bank_name(self) -> str:
        return self._bank_name

    def get_accounts(self) -> list:
        """
        Returns the list of accounts held by the bank.
        """
        return self._accounts

    # ---------- Aggregation Logic ----------

    def add_account(self, account) -> None:
        """
        Adds an account to the banking group.

        :param account: Account object to be added
        """
        if account not in self._accounts:
            self._accounts.append(account)

    def remove_account(self, account) -> None:
        """
        Removes an account from the banking group.

        :param account: Account object to be removed
        """
        if account in self._accounts:
            self._accounts.remove(account)