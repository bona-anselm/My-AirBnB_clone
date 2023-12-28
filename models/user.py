#!/usr/bin/python3
""" Defines the user class """
from models.base_model import BaseModel

class User(BaseModel):
    """ Defines the User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
