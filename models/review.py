#!/usr/bin/python3
"""class Review inherits from BaseModel"""


BaseModel = __import__('base_model').BaseModel


class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        self.place_id = kwargs.pop(Place.id, "")
        self.user_id = kwargs.pop(User.id, "")
        self.text = kwargs.pop(text, "")
