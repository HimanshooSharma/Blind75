"""
https://leetcode.com/problems/valid-anagram/

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_chars = [a for a in s]

        t_chars = [a for a in t]

        s_chars.sort()
        t_chars.sort()

        return s_chars == t_chars
