#!/usr/bin/python3
"""
This script discribes a BaseModel
"""

import uuid
from datetime import datetime
from models import storage

class Basemodel:
    """
    class from which other attributes will inherits and class too
    """

    def __init__(self, *args, **kwargs):
        """
        Initialializing instnace attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = daterime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return official string representation
        """

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containingn all key/values of __dict__
        """

        my_dic = self.__dict__.copy()
        my_dic["__class__"] = type(self).__name__
        my_dic["created_at"] = my_dict["created_at"].isoformat()
        my_dic["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dic
