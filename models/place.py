#!/usr/bin/python3
"""class Place that inherits from Basemodel"""

import models

class Place(models.BaseModel):
    def __init__(self, *args, **kwargs):
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
        if name in ['number_rooms', 'number_bathrooms',
                    'max_guest', 'price_by_night']:
            if isinstance(value, str) and value.isdecimal():
                value = int(value)
                super().__setattr__(self, name, value)
        elif name in ['latitude', 'longitude']:
            if isinstance(value, str) and value.isdecimal():
                value = float(value)
                super().__setattr__(self, name, value)
        else:
            super().__setattr__(self, name, value)
