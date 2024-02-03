#!/usr/bin/python3
import uuid
from datetime import datetime
"""Defines BaseModel module"""


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        d_format = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.strptime(value, d_format))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__

        # Convert datetime objects to string in ISO format
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()

        return result
