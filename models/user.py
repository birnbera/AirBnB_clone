#!/usr/bin/python3
"""class User that inherits from BaseModel"""


BaseModel = __import__('base_model').BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        self.email = kwargs.pop(email, "")
        self.password = kwargs.pop(password, "")
        self.first_name = kwargs.pop(first_name, "")
        self.last_name = kwargs.pop(last_name, "")
        super().__init__(*args, **kwargs)
