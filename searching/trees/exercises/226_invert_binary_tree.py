# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

class Solution:
    # COMPLEXITIES
    #     # Time Complexity: O(N) -> each node is processed once
    #     # Space Complexity: O(N) in the worst case (when the tree is completely unbalanced, meaning the queue holds N/2 nodes at some point).

    def swap_nodes(self, parent):
        if not parent:
            return

        if parent.left:
            self.swap_nodes(parent.left)
        if parent.right:
            self.swap_nodes(parent.right)

        parent.left, parent.right = parent.right, parent.left

        return parent

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.swap_nodes(root)

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # COMPLEXITIES
    #     # Time Complexity: O(N) -> each node is processed once
    #     # Space Complexity: O(N) in the worst case (when the tree is completely unbalanced, meaning the queue holds N/2 nodes at some point).
    #     if not root:
    #         return root

    #     queue = deque([root])

    #     while queue:
    #         node = queue.popleft()
    #         node.left, node.right = node.right, node.left  # Inline swap
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)

    #     return root
