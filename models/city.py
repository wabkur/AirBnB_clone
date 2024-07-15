#!/usr/bin/python3
"""Module to create City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing City."""
    state_id = ""
    name = ""
