#!/usr/bin/python3
""" This module creates Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class for objects of review """

    place_id = ""
    user_id = ""
    text = ""
