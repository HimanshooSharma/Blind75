"""
https://leetcode.com/problems/longest-consecutive-sequence/

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # nums_set = set(nums)

        # longest_sequence = 0

        # for num in nums:
        #     inter_seq_length = 0
        #     if num - 1 not in nums_set:
        #         inter_seq_length +=1
        #         while True:
        #             num += 1
        #             if num in nums_set:
        #                 inter_seq_length +=1
        #             else:
        #                 break
            
        #     if inter_seq_length > longest_sequence:
        #         longest_sequence = inter_seq_length

        # return longest_sequence

        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

