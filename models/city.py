#!/usr/bin/python3
"""class City that inherits from Basemodel"""


BaseModel = __import__('base_model').BaseModel


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        self.state_id = kwargs.pop(State.id, "")
        self.name = kwargs.pop(name, "")
