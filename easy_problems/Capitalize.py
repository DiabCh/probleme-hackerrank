#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    s = s.split(' ')
    srr =''
    for name in s:
        letters = 0
        for letter in name:
            if letter.isalpha() and letters == 0 and name.isalpha():
                srr += letter.upper()
                letters+=1
            else:
                srr += letter
        srr += " "
    return srr
if __name__ == '__main__':


    s = '1 w 2 r 3g'

    result = solve(s)
    print(result)