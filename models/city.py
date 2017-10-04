#!/usr/bin/python3
"""class City that inherits from Basemodel"""

import models


class City(models.BaseModel):
    """Class to implement City"""
    def __init__(self, *args, **kwargs):
        """Initialize new City instance from *args and **kwargs"""
        self.state_id = kwargs.pop('state_id', "")
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
