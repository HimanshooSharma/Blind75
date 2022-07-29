"""
https://leetcode.com/problems/valid-palindrome/
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        return chars == chars[::-1]