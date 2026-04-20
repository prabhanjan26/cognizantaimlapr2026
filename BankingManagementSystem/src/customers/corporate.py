from .customer import Customer


class Corporate(Customer):
    """
    Represents a corporate (business) bank customer.

    A Corporate customer holds business-specific details such
    as company type.
    """

    def __init__(
        self,
        account_number: str,
        name: str,
        company_type: str,
        address: str,
        contact_number: str,
        email: str,
        password: str,
    ):
        """
        Initializes a Corporate customer.

        :param company_type: Type of company (e.g. LTD, PLC)
        """
        super().__init__(
            account_number,
            name,
            address,
            contact_number,
            email,
            password,
        )
        self._company_type = company_type

    # ---------- Getter & Setter ----------

    def get_company_type(self) -> str:
        return self._company_type

    def set_company_type(self, company_type: str) -> None:
        self._company_type = company_type