""""""

from typing import List


class Solution:

    def solve(self, nums, ans, cur, index):
        if index > len(nums):
            return

        ans.append(cur[:])

        for i in range(index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.solve(nums, ans, cur, i)
                cur.pop()

        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solve(nums, ans, cur, 0)

        return ans


if __name__ == '__main__':
    pass
