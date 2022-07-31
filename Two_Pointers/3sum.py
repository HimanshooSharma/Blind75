"""
https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        for i, num in enumerate(nums[:-2]):

            left = i + 1
            right = len(nums) - 1

            if i > 0 and num == nums[i - 1]:
                continue

            while left < right:

                if nums[left] + nums[right] + num == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif nums[left] + nums[right] + num > 0:
                    right -= 1

                else:
                    left += 1

        return res
