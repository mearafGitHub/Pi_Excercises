#!/bin/python3

"""
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
"""

from heapq import *
under = []
upper = []
N = int(input())
for _ in range(N):
    curNumber = int(input())
    if (len(upper) == 0):
        upper.append(curNumber)
        print(curNumber)
        continue
    middle = upper[0]
    if curNumber >= middle:
        heappush(upper,curNumber)
    else:
        heappush(under, -curNumber)
    if len(under) >= len(upper):
        heappush(upper, -heappop(under))
    if len(upper) >= len(under) + 2:
        heappush(under, -heappop(upper))
    if (len(upper) + len(under)) % 2 == 1:
        print(float(upper[0]))
    else:
        print((float(upper[0]) + -under[0])/2)