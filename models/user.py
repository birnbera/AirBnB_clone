#!/usr/bin/python3
"""class User that inherits from BaseModel"""

import models


class User(models.BaseModel):
    """Class to store User info"""
    def __init__(self, *args, **kwargs):
        """Initialize new User instances from *args and **kwargs"""
        self.email = kwargs.pop('email', "")
        self.password = kwargs.pop('password', "")
        self.first_name = kwargs.pop('first_name', "")
        self.last_name = kwargs.pop('last_name', "")
        super().__init__(*args, **kwargs)
