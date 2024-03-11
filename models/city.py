#!/usr/bin/python3

"""This module defines the City model
   Imported from the parent class - Base Model
"""


from models.base_model import BaseModel


class City(BaseModel):
    """Defines the City model"""

    state_id = ""
    name = ""
