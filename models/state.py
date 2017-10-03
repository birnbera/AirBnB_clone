#!/usr/bin/python3
"""class State that inherits from BaseModel"""

import models

class State(models.BaseModel):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
