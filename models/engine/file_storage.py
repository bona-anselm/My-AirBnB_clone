#!/usr/bin/python3
""" Defines a FileStorage class """
import json
from models.base_model import BaseModel


class FileStorage():
    """ Serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            d = {k : v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists ; otherwise, do nothing
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    class_name = o['__class__']
                    del o['__class__']
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return

