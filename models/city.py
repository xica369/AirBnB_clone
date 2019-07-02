#!/usr/bin/python3
""" class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City for create Cities of application
    state_id: string - empty string: it will be the State.id
    name: string - empty string """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ init method call method of the super class
        instantiates a new city"""
        super().__init__(self, *args, **kwargs)
