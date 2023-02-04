#!/usr/bin/python3
"""This module contains a function definition"""
import json


def from_json_string(my_str):
    """This function deserializes an object from a JSON string"""
    return json.loads(my_str)
