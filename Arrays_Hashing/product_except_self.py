"""
https://leetcode.com/problems/product-of-array-except-self/

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # This is a tricky one

        res = [1 for i in range(len(nums))]

        prefix, suffix = 1, 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
