#!/usr/bin/python3
"""Module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class managing a Review."""
    place_id = ""
    user_id = ""
    text = ""
