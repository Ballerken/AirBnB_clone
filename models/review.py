#!/usr/bin/python3

"""This module defines the Review model
   Imported from the parent class - Base Model
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review model"""

    place_id = ""
    user_id = ""
    text = ""
