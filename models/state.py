#!/usr/bin/python3
"""class State that inherits from BaseModel"""


BaseModel = __import__('base_model').BaseModel


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop(name, "")
