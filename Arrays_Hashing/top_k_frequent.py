"""
https://leetcode.com/problems/top-k-frequent-elements/

"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        result = []

        frequency = [[] for i in range(len(nums) + 1)]

        for num, count in count_map.items():
            frequency[count].append(num)

        for freq in frequency[::-1]:
            if len(freq) == 0:
                continue
            for num in freq:
                if len(result) == k:
                    break
                result.append(num)

        return result
