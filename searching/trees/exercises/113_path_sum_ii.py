# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        stack = [(root, [root.val])]
        paths = []

        while stack:
            curr_node, curr_path = stack.pop()

            if (
                not curr_node.left
                and not curr_node.right
                and sum(curr_path) == targetSum
            ):
                paths.append(curr_path)

            if curr_node.right:
                stack.append((curr_node.right, curr_path + [curr_node.right.val]))

            if curr_node.left:
                stack.append((curr_node.left, curr_path + [curr_node.left.val]))

        return paths
