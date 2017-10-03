#!/usr/bin/python3
"""class BaseModel"""

import models
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for k, v in kwargs.items():
            """searches through dict for keys"""
            if k in ['created_at', 'updated_at']:
                try:
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                except:
                    print("cannot set datetime with: {}".format(v))
                    raise
            elif k == "__class__":
                continue
            setattr(self, k, v)
        if "id" not in kwargs:
            models.storage.new(self)

    def __setattr__(self, name, value):
        if name in ['created_at', 'updated_at']:
            if isinstance(value, str):
                try:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                except:
                    print("cannot set datetime with: {}".format(value))
                    return
        super().__setattr__(name, value)

    def __str__(self):
        """returns __str__ method"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all k/v of __dict__"""
        d = {}
        d.update(self.__dict__)
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        d['__class__'] = self.__class__.__name__
        return d
