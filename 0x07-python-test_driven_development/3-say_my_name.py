#!/usr/bin/python3
""" define a name printing function"""
def say_my_name(first_name, last_name)
"""
Prints the full name in the format: "My name is <first_name> <last_name>".

    Parameters:
        first_name (str): The first name.
        last_name (str): The last name, defaults to an empty string if not provided.

    Raises:
        TypeError: If either first_name or last_name is not a string.
"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"my name is {first_name} {last_name}")
