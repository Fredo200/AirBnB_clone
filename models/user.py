#!/usr/bin/python3
""" This creates User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class for objects of user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
