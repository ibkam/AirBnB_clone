#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""Defines BaseModel module"""


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        if kwargs:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
            if "created_at" not in kwargs:
                kwargs["created_at"] = datetime.now().isoformat()
            if "updated_at" not in kwargs:
                kwargs["updated_at"] = datetime.now().isoformat()

            for key, value in kwargs.items():
                if key == 'updated_at':
                    kwargs[key] = datetime.strptime(
                        value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'created_at':
                    kwargs[key] = datetime.strptime(
                        value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                if hasattr(self, key) and key != '__class__':
                    setattr(self, key, value)

            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
            
    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        for key in self.__dict__.keys():
            if key == "_sa_instance_state":
                del (dictionary[key])

        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        
        return dictionary
