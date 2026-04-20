from datetime import date
from .customer import Customer


class Individual(Customer):
    """
    Represents an individual (personal) bank customer.

    An Individual customer has personal attributes such as
    surname, gender, and date of birth, and can calculate
    their age.
    """

    def __init__(
        self,
        account_number: str,
        name: str,
        surname: str,
        gender: str,
        date_of_birth: date,
        address: str,
        contact_number: str,
        email: str,
        password: str,
    ):
        """
        Initializes an Individual customer.

        :param surname: Customer's surname
        :param gender: Customer's gender
        :param date_of_birth: Customer's date of birth
        """
        super().__init__(
            account_number,
            name,
            address,
            contact_number,
            email,
            password,
        )
        self._surname = surname
        self._gender = gender
        self._date_of_birth = date_of_birth

    # ---------- Getters & Setters ----------

    def get_surname(self) -> str:
        return self._surname

    def set_surname(self, surname: str) -> None:
        self._surname = surname

    def get_gender(self) -> str:
        return self._gender

    def set_gender(self, gender: str) -> None:
        self._gender = gender

    def get_date_of_birth(self) -> date:
        return self._date_of_birth

    # ---------- Business Logic ----------

    def work_out_age(self) -> int:
        """
        Calculates and returns the customer's age.
        """
        today = date.today()
        age = today.year - self._date_of_birth.year

        if (today.month, today.day) < (
            self._date_of_birth.month,
            self._date_of_birth.day,
        ):
            age -= 1

        return age