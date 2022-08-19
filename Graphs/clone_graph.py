"""
https://leetcode.com/problems/clone-graph/
"""

# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        old_to_new = {}

        def clone(node):

            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node)
