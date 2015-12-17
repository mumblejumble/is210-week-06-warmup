#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""using for loop to reverse the inner sequence"""


def flip_keys(to_flip):
    """This function returns a list with inner list sequence flipped.

    Args:
        to_flip(list): could be passed with interger or string.

    Returns:
        returns a list with flipped inner sequence

    Examples:
        >>>LIST = [(1, 2, 3), 'abc']
        >>>NEW = flip_keys(LIST)
        >>>LIST is NEW
        True
        >>>print LIST
        [(3,2,1), 'cba']
    """
    counter = 0
    for flipvar in to_flip:
        re_myvar = (flipvar[::-1])
        to_flip[counter] = re_myvar
        counter += 1
    return to_flip
