"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""
def getFirstPosition(nums, target):

    left = 0
    right = len(nums)-1

    first = -1
    last = -1

    while left<=right:
        mid = (left+right)//2

        if nums[mid] == target:
            if mid==0 or nums[mid-1]!=target:
                return mid
            right = mid-1
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return -1

def getLastPosition(nums, target):

    left = 0
    right = len(nums)-1

    while left<=right:
        mid = (left+right)//2

        if nums[mid] == target:
            if mid==len(nums)-1 or nums[mid+1]!=target:
                return mid
            left = mid+1
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return -1

def searchRange(nums, target):

    first = getFirstPosition(nums, target)

    if first == -1:
        return [first, first]

    last = getLastPosition(nums, target)

    return [first, last]

if __name__ == '__main__':
    x = [5,7,7,8,8,10]
    t = 8

    r = searchRange(x, t)

    print(r)
