#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    res=s[:len(s)-2:]
    if 'AM' in s:
        if s[:2:]=='12':
            res="00"+s[2:len(s)-2:]
    else:
        if s[:2:]!='12':
            res=str(int(s[:2:])+12)+s[2:len(s)-2:]
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
