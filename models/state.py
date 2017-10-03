#!/usr/bin/python3
"""class State that inherits from BaseModel"""

import models


class State(models.BaseModel):
    """Class to store State info"""
    def __init__(self, *args, **kwargs):
        """Initialize new State instance from *args and **kwargs"""
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
