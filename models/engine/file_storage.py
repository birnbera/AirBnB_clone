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
        with open(__file_path, 'w') as f:
            json.dump(self.all(), f)

    def reload(self):
        try:
            with open(__file_path, 'r') as f:
                self.__objects = json.load(f)
        except:
            pass
