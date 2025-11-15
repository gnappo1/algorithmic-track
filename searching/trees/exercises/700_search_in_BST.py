# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Time: O(h)
        # Space: O(h) for recursion stack

        # DFS
        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# ================================
# iterative, pointer based DFS
# if not root:
#     return None

# curr = root

# while curr:

#     if curr.val == val:
#         return curr

#     if val < curr.val:
#         curr = curr.left
#     else:
#         curr = curr.right


# return None
