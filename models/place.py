#!/usr/bin/python3

"""This module defines the Place model
   Imported from the parent class - Base Model
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the Place model."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
