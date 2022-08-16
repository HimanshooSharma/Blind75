"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left_boundry, right_boundry):
            if not node:
                return True
            
            if not (node.val < right_boundry and node.val > left_boundry):
                return False

            return (valid(node.left, left_boundry, node.val) and 
                valid(node.right, node.val, right_boundry))

        return valid(root, float("-inf"), float("inf"))