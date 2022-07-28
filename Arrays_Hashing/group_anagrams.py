"""
https://leetcode.com/problems/group-anagrams/

"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for word in strs:

            hash_map[str(sorted(word))].append(word)

        return hash_map.values()
