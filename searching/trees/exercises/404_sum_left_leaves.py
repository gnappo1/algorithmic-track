# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], use=False) -> int:
        # DFS with custom stack

        if not root:
            return 0

        tot = 0
        stack = deque([(root, False)])

        while stack:
            node, use = stack.pop()

            if not node.left and not node.right and use:
                tot += node.val

            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))

        return tot

        # DFS internal stack

        # if not root:
        #     return 0

        # if not root.left and not root.right:
        #     return root.val if use else 0

        # return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
