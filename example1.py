import math
import os
import random
import re
import sys

def findNumber(arr, k):
    # Write your code here
    return arr

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'lala.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findNumber(arr, k)

    fptr.write(result + '\n')

    fptr.close()