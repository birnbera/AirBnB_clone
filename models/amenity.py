#!/usr/bin/python3
"""class Amenity that inherits from BaseModel"""


BaseModel = __import__('base_model').BaseModel


class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop(name, "")
