"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

def firstBadVersion(n):
    left = 1
    right = n

    while left<right:
        mid = left + (right-left)//2

        if not isBadVersion(mid):
            left = mid+1
        else:
            right = mid

    return left

Solution to https://leetcode.com/problems/first-bad-version/
"""
def firstBadVersion(n, bad):
    left = 1
    right = n

    while left<right:
        mid = left + (right-left)//2

        if not isBadVersion(mid, bad):
            left = mid+1
        else:
            right = mid

    return left

def isBadVersion(n, bad):
    return n>=bad

if __name__ == '__main__':

    print("*")
    print(firstBadVersion(6, 3))
    print("*")
