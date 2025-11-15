# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
        
        lh = left_height(root)
        rh = right_height(root)
        
        if lh == rh:
            # perfect tree
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        #======================
        # DFS
        # Time: O(N)
        # Space: O(H) -> logN or N for skewed trees

        # if not root:
        #     return 0
        
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        #================
        # BFS leveraging the height but not a real optimization
        # def height(node):
        #     if not node:
        #         return 0
            
        #     left_h = height(node.left)
        #     right_h = height(node.right)

        #     return 1 + max(left_h, right_h)
        
        # if not root:
        #     return 0

        # max_depth = height(root) - 1

        # queue = deque([(root, 0)])
        # count = 2 ** (max_depth) - 1

        # while queue:
        #     node, h = queue.popleft()

        #     if not node:
        #         continue

        #     if h < max_depth:
        #         queue.append((node.left, h + 1))
        #         queue.append((node.right, h + 1))
        #     else:
        #         count += 1

        # return count 
