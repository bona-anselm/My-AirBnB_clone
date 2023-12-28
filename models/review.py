#!/usr/bin/python3
""" Defines Review class """
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""
