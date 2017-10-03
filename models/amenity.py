#!/usr/bin/python3
"""class Amenity that inherits from BaseModel"""

import models


class Amenity(models.BaseModel):
    """Class to store Amenities"""
    def __init__(self, *args, **kwargs):
        """Initialize new instance from *args and **kwargs"""
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
