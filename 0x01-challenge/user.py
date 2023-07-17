#!/usr/bin/python3
"""
Create and define a class - 'User'
"""


class User():
    """ Define and initialize a user() object """

    def __init__(self):
        """Initialize user() objects"""
        self.__email = None

    @property
    def email(self):
        """Get the email of user() object"""
        return (self.__email)

    @email.setter
    def email(self, value):
        """Set the email of user() object
        Arg:
            value: represent the value to which user() email is to be set
        Exceptions:
            TypeError: if value passed is not a string
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
