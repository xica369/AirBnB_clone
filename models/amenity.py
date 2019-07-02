#!/usr/bin/python3
""" class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity for create amenities of application
    name: string - empty string """
    name = ""

    def __init__(self, *args, **kwargs):
        """ init method call method of the super class
        instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
