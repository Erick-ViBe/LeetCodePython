"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example:

Input: nums = [3,2,4], target = 7
Output: [0,2]
"""

def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        goal = target-nums[i]

        if goal in m:
            return [m[goal], i]

        m[nums[i]] = i


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6

    print("*")
    print(twoSum(nums, target))
    print("*")
