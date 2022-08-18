"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        
        def preorder(root):
            if not root:
                serialized.append('N')
                return

            serialized.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return ','.join(serialized)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        i = 0

        def decode():
            nonlocal i
            if vals[i] == 'N':
                i += 1
                return None
            
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = decode()
            node.right = decode()
            return node

        root = decode()

        return root