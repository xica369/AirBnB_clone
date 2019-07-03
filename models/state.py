#!/usr/bin/python3
""" class State """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class State for create states of application
    name: string - empty string """
    name = ""

    def __init__(self, *args, **kwargs):
        """ init method call method of the super class
        instantiates a new state """
        super().__init__(self, *args, **kwargs)
