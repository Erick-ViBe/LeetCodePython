"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?


Example:

Input: nums = [2,2,1]
Output: 1
"""

def SingleNumber(nums):
    rep = []
    for x in nums:
        if x in rep:
            rep.remove(x)
        else:
            rep.append(x)

    return rep[0]


def singleNumber2(nums):
    return 2*sum(set(nums))-sum(nums)


if __name__ == '__main__':
    x = [1, 2, 1]

    print("*")
    print(SingleNumber(x))
    print("*")
    print(singleNumber2(x))
    print("*")
