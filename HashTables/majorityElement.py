"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

def majorityElement(nums):
    m = {}

    for x in nums:
        m[x] = m.get(x, 0) + 1

    for x in nums:
        if m[x] > len(nums)//2:
            return x


def majorityElement2(nums):
    m = {}

    for x in nums:
        m[x] = m.get(x, 0) + 1

    for x in m:
        if m[x] > len(nums)//2:
            return x


def majorityElement3(nums):
        s=set(nums)
        for i in s:
            if nums.count(i) > len(nums)//2:
                return i

if __name__ == '__main__':
    x = [2,2,1,1,1,2,2]

    print("*")
    print(majorityElement(x))
    print("*")
    print(majorityElement2(x))
    print("*")
