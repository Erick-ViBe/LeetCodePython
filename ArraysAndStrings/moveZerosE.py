"""
Given an array of integers, write a function to
move all 0's to the end while maintaining the
relative order of the other elements
"""
def moveZeroes(nums):
    j = 0

    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1

    for x in range(j, len(nums)):
        nums[x] = 0

    return nums


if __name__ == '__main__':
    x = [0, 1, 0, 3, 12]

    result = moveZeroes(x)

    print (result)
