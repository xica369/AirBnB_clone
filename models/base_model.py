#!/usr/bin/python3
""" class Base Model """
from uuid import uuid4
import models
from datetime import datetime


class BaseModel():
    """ Super class model for class application """

    def __init__(self, *args, **kwargs):
        """init function of BaseModel
        if **kwargs is not empty create a new instance whit
        the values sended
        else create a new instance with the default values"""
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance """
        new_dict = {}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                new_dict[key] = self.__dict__[key].isoformat()
            else:
                new_dict[key] = self.__dict__[key]
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        '''Generate a string object
        Return: a string with the information of the object'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
