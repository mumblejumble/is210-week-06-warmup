#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""using for loop to reverse the inner sequence"""


def flip_keys(to_flip):
    """using for loop to reverse the order of the inner sequence

    args:
        to_flip(list): could be passed with interger or string.

        for loop: every item's inner sequence in given list is flipped

    returns:
        returns a list with flipped inner sequence

    examples:
        >>>LIST = [(1, 2, 3), 'abc']
        >>>NEW = flip_keys(LIST)
        >>>LIST is NEW
        True
        >>>print LIST
        [(3,2,1), 'cba']
    """

    counter = 0

    for flipvar in to_flip:
        mylistvar = (flipvar[::-1])
        to_flip[counter] = mylistvar
        counter += 1

    return to_flip
