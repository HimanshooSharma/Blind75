"""
https://leetcode.com/problems/two-sum/

"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums[:-1]):
            if target - num in nums[i + 1 :]:
                return [i, i + 1 + nums[i + 1 :].index(target - num)]

        # more explainable solution

        # prevMap = {}  # val -> index

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
