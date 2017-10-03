#!/usr/bin/python3
"""class City that inherits from Basemodel"""

import models

class City(models.BaseModel):
    def __init__(self, *args, **kwargs):
        self.state_id = kwargs.pop('state_id', "")
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
