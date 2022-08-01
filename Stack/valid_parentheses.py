"""
https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {')':'(',']':'[','}':'{'}

        stack = []

        for c in s:
            if c not in bracket_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != bracket_map[c]:
                return False
            stack.pop()

        return not stack # True when stach is empty