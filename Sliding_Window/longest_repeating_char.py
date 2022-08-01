"""
https://leetcode.com/problems/longest-repeating-character-replacement/
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_count = {}

        left = 0
        res = 0
        most_frequent = 0

        for right in range(len(s)):
            char_count[s[right]] = 1 + char_count.get(s[right], 0)
            most_frequent = max(most_frequent, char_count[s[right]])

            if (right - left + 1) - most_frequent > k:
                char_count[s[left]] -= 1
                left += 1
                

            res = max(res, right - left + 1)

        return res
