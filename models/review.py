#!/usr/bin/python3
"""class Review inherits from BaseModel"""

import models


class Review(models.BaseModel):
    """Class to store Reviews"""
    def __init__(self, *args, **kwargs):
        """Initialize new Review instance from *args and **kwargs"""
        self.place_id = kwargs.pop('place_id', "")
        self.user_id = kwargs.pop('user_id', "")
        self.text = kwargs.pop('text', "")
        super().__init__(*args, **kwargs)
