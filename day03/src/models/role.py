"""Role model definition for the healthcare application."""
class Role:
    """ A class representing a role with a name and description. """
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        """Get the role's name."""
        return self.__name

    @property
    
    def description(self):
        """Get the role's description."""
        return self.__description
    #setter for description with validation
    @description.setter
    def description(self, value):
        self.__description = value