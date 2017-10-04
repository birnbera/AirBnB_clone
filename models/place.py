#!/usr/bin/python3
"""Implements class Place that inherits from Basemodel"""

import models


class Place(models.BaseModel):
    """Class to store place information"""
    def __init__(self, *args, **kwargs):
        """Initialize new instance of Place from *args and **kwargs"""
        self.city_id = kwargs.pop('city_id', "")
        self.user_id = kwargs.pop('user_id', "")
        self.name = kwargs.pop('name', "")
        self.description = kwargs.pop('description', "")
        self.number_rooms = kwargs.pop('number_rooms', 0)
        self.number_bathrooms = kwargs.pop('number_bathrooms', 0)
        self.max_guest = kwargs.pop('max_guest', 0)
        self.price_by_night = kwargs.pop('price_by_night', 0)
        self.latitude = kwargs.pop('latitude', 0.0)
        self.longitude = kwargs.pop('longitude', 0.0)
        self.amenity_ids = kwargs.pop('amenity_id', [])
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Maintain correct types for non-string attributes while keeping
        the attributes as public attributes.

        Args:
            name (str): name of attribute
            value: value to associate with `name`

        Raises:
            AttributeError: If value cannot be parsed into correct format
        """
        if name in ['number_rooms', 'number_bathrooms',
                    'max_guest', 'price_by_night']:
            try:
                value = int(value)
            except ValueError:
                raise AttributeError("Invalid value: ({}) for name: ({})"
                                     .format(value, name))
        elif name in ['latitude', 'longitude']:
            try:
                value = float(value)
            except ValueError:
                raise AttributeError("Invalid value: ({}) for name: ({})"
                                     .format(value, name))
        super().__setattr__(name, value)
