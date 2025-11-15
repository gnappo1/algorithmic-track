# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # first leaf we see is at minimum depth
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


# ================
# DFS - custom

# if not node:
#     return 0

# global_min = 10**5 + 1
# stack = deque([(node, 1)])

# while stack:
#     curr, depth = stack.pop()

#     if not curr.left and not curr.right:
#         global_min = min(global_min, depth)

#     if curr.right:
#         stack.append((curr.right, depth+1))

#     if curr.left:
#         stack.append((curr.left, depth+1))

# return global_min

# ================
# DFS - classic

# if not node:
#     return 0

# if not node.left:
#     return 1 + self.minDepth(node.right)
# if not node.right:
#     return 1 + self.minDepth(node.left)

# return 1 + min(self.minDepth(node.left), self.minDepth(node.right))
