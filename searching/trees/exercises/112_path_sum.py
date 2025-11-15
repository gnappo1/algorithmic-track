# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, curr=0) -> bool:
        # Time Complexity: O(N) in the worst case (visiting all nodes).
        # Space Complexity: O(H) (where H is the height of the tree), since the stack will hold at most H elements at once.
        # In the worst case (skewed tree), it's O(N), and for a balanced tree, it's O(log N).

        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:
            node, count = queue.pop()

            if not node.left and not node.right and count == targetSum:
                return True

            if node.right:
                queue.append((node.right, count + node.right.val))
            if node.left:
                queue.append((node.left, count + node.left.val))

        return False

        # DFS using internal stack

        # if not root:
        #     return False

        # if not root.left and not root.right:
        #     return curr + root.val == targetSum

        # return  (
        #     self.hasPathSum(root.left, targetSum, curr + root.val)
        #     or
        #     self.hasPathSum(root.right, targetSum, curr + root.val)
        # )
