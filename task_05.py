#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""using for loop to reverse the inner sequence"""


def flip_keys(to_flip):
    """using for loop to reverse the order of the inner sequence

    arguments:
        REVERSED: reversing inner sequence in given list

        for loop: every item's inner sequence in given list is flipped

    returns:
        returns a list with flipped inner sequence

    examples:
        >>>print LIST
        [(3,2,1), 'cba']
    """

    counter = 0

    for stuff in to_flip:
        REVERSED = stuff[::-1]
        to_flip[counter] = REVERSED
        counter += 1
        counter == len(to_flip)

    return to_flip

LIST = [(1,2,3), 'abc']
