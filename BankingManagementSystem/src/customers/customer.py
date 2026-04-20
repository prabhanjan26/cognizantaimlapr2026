from abc import ABC


class Customer(ABC):
    """
    Abstract base class representing a bank customer.

    A customer holds personal or business details and may own
    one or more bank accounts. This class provides shared attributes
    and behaviour for all customer types.
    """

    _total_customers = 0  # class variable to track total customers

    def __init__(
        self,
        account_number: str,
        name: str,
        address: str,
        contact_number: str,
        email: str,
        password: str,
    ):
        """
        Initializes a Customer object.

        :param account_number: Unique customer account number
        :param name: Customer's full name
        :param address: Customer's address
        :param contact_number: Customer's contact phone number
        :param email: Customer's email address
        :param password: Customer's login password
        """
        self._account_number = account_number
        self._name = name
        self._address = address
        self._contact_number = contact_number
        self._email = email
        self._password = password

        Customer._total_customers += 1

    # ---------- Getters & Setters ----------

    def get_account_number(self) -> str:
        return self._account_number

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_address(self) -> str:
        return self._address

    def set_address(self, address: str) -> None:
        self._address = address

    def get_contact_number(self) -> str:
        return self._contact_number

    def set_contact_number(self, contact_number: str) -> None:
        self._contact_number = contact_number

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str) -> None:
        self._email = email

    def get_password(self) -> str:
        return self._password

    def set_password(self, password: str) -> None:
        self._password = password

    # ---------- Class Method ----------

    @classmethod
    def total_number_of_customers(cls) -> int:
        """
        Returns the total number of customers created.
        """
        return cls._total_customers