#!/usr/bin/python3
"""Implements class Place that inherits from Basemodel"""

import models


class Place(models.BaseModel):
    """Class to store place information"""
    city_id = 'city_id', "")
    user_id = 'user_id', "")
    name = 'name', "")
    description = 'description', "")
    number_rooms = 'number_rooms', 0)
    number_bathrooms = 'number_bathrooms', 0)
    max_guest = 'max_guest', 0)
    price_by_night = 'price_by_night', 0)
    latitude = 'latitude', 0.0)
    longitude = 'longitude', 0.0)
    amenity_ids = 'amenity_id', [])
