"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0

        left = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right

            max_p = max(max_p, prices[right] - prices[left])

        return max_p
