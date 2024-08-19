#!/usr/bin/python
"""
Contains:
    Functions
    =========
    validUTF8 - Receives a list of integers and checks if
    the list represents a valid utf-8 encoding or not.
"""
from typing import List


def convert_to_binary(num: int) -> str:
    """Converts given integer to binary"""
    binary = bin(num)[2:]
    if len(binary) > 8:
        return binary[len(binary) - 8:]
    return ("0" * (8 - len(binary))) + binary


def construct_binary_representation(data: List[int]) -> str:
    """
    Receives a list of integers and returns a list
    of the binary representation of each integer in the list
    """
    return [convert_to_binary(num) for num in data]


def validate_bytes(bytes_list: List[str]):
    """
    Validates that a sequence of bytes is valid utf-8
    encoding
    """
    bool_list = [repr.startswith("10") for repr in bytes_list]
    return all(bool_list)


def validUTF8(data: List[int]) -> bool:
    """
    Receives a list of integers and checks if
    the list represents a valid utf-8 encoding or not.

    Args:
        data (list): A list of integers to be checked for
        utf-8 validity

    Returns:
        (bool): True if the data represents valid utf-8
        encoding, False otherwise
    """
    binary_repr = construct_binary_representation(data)
    print(binary_repr)
    idx = 0
    while idx < len(binary_repr):
        repr = binary_repr[idx]
        if repr[0] == '1':
            i = 0
            while i < len(repr) and repr[i] == '1':
                i += 1
            try:
                assert 4 >= i > 1
                assert repr[i] == '0'
                assert idx + i <= len(binary_repr)
            except Exception:
                return False
            if not validate_bytes(binary_repr[idx+1:idx+i]):
                return False
            idx += i - 1
        idx += 1
    return True
