"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

    - A.length >= 3

    - There exists some i with 0 < i < A.length - 1 such that:
        + A[0] < A[1] < ... A[i-1] < A[i]
        + A[i] > A[i+1] > ... > A[A.length - 1]
"""

def validMountainArray(arr):
    if len(arr) < 3:
        return False

    i = 1

    while i<len(arr) and arr[i]>arr[i-1]:
        i += 1

    if i==len(arr) or i == 1:
        return False

    while i<len(arr) and arr[i]<arr[i-1]:
        i += 1

    return i==len(arr)


if __name__ == '__main__':
    mountain = [0, 2, 3, 4, 5, 2, 1]

    result = validMountainArray(mountain)

    print(result)
