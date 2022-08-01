"""
https://leetcode.com/problems/minimum-window-substring/
"""

# Deceptively Hard Problem


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        left = 0

        count_T, count_window = {}, {}

        res, res_length = [-1, -1], float("infinity")

        for c in t:
            count_T[c] = 1 + count_T.get(c, 0)

        have = 0
        need = len(count_T)

        for right in range(len(s)):

            c = s[right]
            count_window[c] = 1 + count_window.get(c, 0)

            if c in count_T and count_window[c] == count_T[c]:
                have += 1

            while have == need:

                if (right - left + 1) < res_length:
                    res = [left, right]
                    res_length = right - left + 1

                count_window[s[left]] -= 1
                if s[left] in count_T and count_window[s[left]] < count_T[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return s[l : r + 1] if res_length != float("infinity") else ""
