"""
https://leetcode.com/problems/number-of-islands/
"""

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        nu_of_islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))

            q.append((r, c))
            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

            while q:
                row, col = q.popleft()
                for row_dir, col_dir in directions:
                    curr_row = row + row_dir
                    curr_col = col + col_dir

                    if (
                        curr_row in range(rows)
                        and curr_col in range(columns)
                        and grid[curr_row][curr_col] == "1"
                        and (curr_row, curr_col) not in visited
                    ):
                        q.append((curr_row, curr_col))
                        visited.add((curr_row, curr_col))

        for row in range(rows):
            for column in range(columns):
                if (row, column) not in visited and grid[row][column] == "1":
                    bfs(row, column)
                    nu_of_islands += 1

        return nu_of_islands
