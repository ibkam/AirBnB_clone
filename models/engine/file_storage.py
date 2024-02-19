#!/usr/bin/python3
"""
Contains the file_storage class model
"""


import json
import models


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects
        """
        if cls is not None:
            return self.__objects
        else:
            filtered_obj = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    filtered_obj[key] = value
        return filtered_obj

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """
       self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes obj from objects"""
        if obj is not None:
            key = key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()


    def save(self):
        """
        serializes __objects to the JSON file
        """
        serialized_objects = {}
        for key, val in self.__objects.items():
            serialized_objects[key] = val.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
                
                for key, val in self.__objects.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
            
    def close(self):
        """Deserialize the JSON file to objects"""
        self.reload()
