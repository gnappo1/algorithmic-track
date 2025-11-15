# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(
        self, root: TreeNode, low=float("-inf"), high=float("inf")
    ) -> bool:
        # Time: O(n), every node is visited once.
        # Space: O(n) in the worst case
        if not root:
            return True

        if not low < root.val < high:
            return False

        return self.isValidBST(root.left, low, root.val) and self.isValidBST(
            root.right, root.val, high
        )

        # from functools import deque
        # if not root:
        #     return True

        # queue = deque([(root, float("-inf"), float("inf"))])

        # while queue:
        #     node, min_v, max_v = queue.popleft()

        #     if not min_v < node.val < max_v:
        #         return False

        #     if node.right:
        #         queue.append((node.right, node.val, max_v))

        #     if node.left:
        #         queue.append((node.left, min_v, node.val))

        # return True
