#!/usr/bin/python3
""" This module creates User class """

from models.base_model import BaseModel


class City(BaseModel):
    """ Class for objects of City """

    state_id = ""
    name = ""

