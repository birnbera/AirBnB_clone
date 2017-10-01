#!/usr/bin/python3
"""class BaseModel"""

from models import storage
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for k, v in kwargs.items():
            if k in ['created_at', 'updated_at']:
                v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
            if k == "__class__":
                continue
            setattr(self, k, v)
        if "id" not in kwargs:
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        d = {}
        d.update(self.__dict__)
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        d['__class__'] = self.__class__.__name__
        return d
