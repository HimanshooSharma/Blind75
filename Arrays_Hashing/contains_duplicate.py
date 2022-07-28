"""
https://leetcode.com/problems/contains-duplicate

"""


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Solution 01

        # nums.sort()
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True

        # return False

        # Solution 02

        # nums_set = set(nums)

        # return len(nums_set) != len(nums)

        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True

        return False
