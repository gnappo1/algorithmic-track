# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Thesis
    # 1. Is the tree balanced

    # Hypothesis
    # 0. The tree is a Binary Tree
    # 1. The number of nodes in the tree is in the range [0, 5000]
    # 2. -10^4 <= Node.val <= 10^4

    # Conclusions on Complexities
    # Recursive DFS postorder approach (left, right, center)
    # Time: O(N) we visit every node once only
    # Space: O(H) we need to cache in the stack at worst each function call along the longest path. O(H) can be O(N) if the tree is skewed (bad), or O(logN) if the tree is balanced

    def check_height(self, node):
        # express the base case
        if not node:
            return True, 0

        is_left_balanced, left_height = self.check_height(node.left)

        if not is_left_balanced:
            return False, left_height

        is_right_balanced, right_height = self.check_height(node.right)

        if not is_right_balanced:
            return False, right_height

        is_balanced = abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1

        return is_balanced, height

    def isBalanced(self, root: TreeNode) -> bool:
        is_balanced, height = self.check_height(root)
        return is_balanced
