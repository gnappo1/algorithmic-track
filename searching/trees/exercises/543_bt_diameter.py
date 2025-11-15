# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def __init__(self):
        self.diameter = 0

    def check_heights(self, node):
        if not node:
            return 0

        left_height = self.check_heights(node.left)
        right_height = self.check_heights(node.right)

        self.diameter = max(left_height + right_height, self.diameter)

        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.check_heights(root)
        return self.diameter
