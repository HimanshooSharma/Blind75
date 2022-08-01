"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring_set = set()

        left = 0

        longest_substring = 0

        for right in range (len(s)):
            while s[right] in substring_set:
                substring_set.remove(s[left])
                left += 1

            substring_set.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring
