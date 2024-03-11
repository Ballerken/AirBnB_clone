#!/usr/bin/python3

"""
Module: test_methods.py
Description: Defines useful short methods that are used during testing
"""

from io import StringIO
from uuid import UUID as uuid
from random import choice


class Test_Methods:
    """Defines useful short methods that are heavily used during testing."""

    # Define random attributes for testing
    __random_attributes = {
        "first_name": ["Nancy", "Adenike", "Afua", "Alfred", "Kennedy"],
        "last_name": ["Nengi", "Bamidele", "Anaglate", "Boamah", "Asare"],
        "age": [26, 20, 21, 25, 23, 26]
    }

    @staticmethod
    def get_uuid(line: StringIO) -> uuid:
        """Returns the UUID from a string."""
        return uuid(line.getvalue().strip())

    @staticmethod
    def get_instances_count(line: StringIO) -> int:
        """Returns the integer value for the number of instances of a model."""
        return int(line.getvalue().strip())

    @staticmethod
    def get_key(model_name: str, instance_id: uuid) -> str:
        """Generates the key used in the objects dictionary for an instance."""
        return f"{model_name}.{instance_id}"

    def get_first_name(self) -> str:
        """Returns a first name."""
        return choice(self.__random_attributes["first_name"])

    def get_last_name(self) -> str:
        """Returns a first name."""
        return choice(self.__random_attributes["last_name"])

    def get_email(self, first_name: str = None, last_name: str = None) -> str:
        """Returns an email address based on random first and last names."""
        return (
            f"{first_name or self.get_first_name()}."
            f"{last_name or self.get_last_name()}@lzcorp.it".lower()
        )

    def get_random_attribute(self):
        """Generates a random key and a value corresponding to that key."""
        key = choice(list(self.__random_attributes.keys()))

        return key, choice(self.__random_attributes[key])


if __name__ == "__main__":
    instance = Test_Methods()

    print(instance.get_random_attribute())
