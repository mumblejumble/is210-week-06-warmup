#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Applying for loop"""


def process_data(data):
    """returns a tuple of the sum and the mean for a given dataset

    args:
        data: could be passed by integers.

    returns:
        returns sum of dataset and mean of the dataset as a tuple

    examples:
        process_data([1,2,3])
        >>>(6, 2.0)
    """
    mysum = 0
    for mynum in data:
        mysum += mynum
    myave = mysum/float(len(data))
    return mysum, myave
