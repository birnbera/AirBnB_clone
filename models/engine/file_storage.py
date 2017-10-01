#!/usr/bin/python3
"""Store first object"""

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            for name, obj in self.__objects.items():
                self.__objects[name] = obj.to_dict()
            json.dump(self.all(), f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f, object_hook=self.models_obj_hook)
        except:
            pass

        """
        else:
            for name, obj_dict in self.__objects.items():
                self.__objects[name] = eval(obj['__class__'])(**obj)
        """

    @staticmethod
    def models_obj_hook(o_dict):
        if '__class__' in o_dict:
            if o_dict['__class__'] == 'BaseModel':
                from models.base_model import BaseModel
                return BaseModel(**o_dict)
            else:
                return o_dict
        else:
            return o_dict
