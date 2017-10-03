#!/usr/bin/python3
"""class Review inherits from BaseModel"""

import models

class Review(models.BaseModel):
    def __init__(self, *args, **kwargs):
        self.place_id = kwargs.pop('place_id', "")
        self.user_id = kwargs.pop('user_id', "")
        self.text = kwargs.pop('text', "")
        super().__init__(*args, **kwargs)
