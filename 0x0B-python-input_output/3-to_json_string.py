#!/usr/bin/python3
"""This module contains a function definition"""
import json


def to_json_string(my_obj):
    """This function serializes an object to a JSON string"""
    return json.dumps(my_obj)
