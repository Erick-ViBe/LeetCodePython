"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false
"""

def containsDuplicate(nums):
    return len(nums) != len(set(nums))


def containsDuplicate2(nums):
    n = len(nums)-1
    nums.sort()

    for i in range(n):
        if nums[i] == nums[i+1]:
            return True

    return False


def containsDuplicate3(nums):
    m = {}

    for x in nums:
        if x in m:
            return True
        m[x] = 1

    return False


if __name__ == '__main__':
    x = [1,2,3,4]

    print("*")
    print(containsDuplicate(x))
    print("*")
    print(containsDuplicate2(x))
    print("*")
    print(containsDuplicate3(x))
    print("*")
