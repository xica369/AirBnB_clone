#!/usr/bin/python3
""" class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User for create users of application """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ init method call method of the super class
        instantiates a new user """
        super().__init__(self, *args, **kwargs)
