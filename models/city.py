#!/usr/bin/python3
""" Defines State class """
from models.base_model import BaseModel
import models


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""
