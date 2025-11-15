# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Iterative In-order traversal (DFS)
        # this way we can early return when we find the kth smallest element rather then computing the entire array fir the ordered tree
        # Time: still O(h + k), worst case O(n), but you can stop early, without traversing everything if k is small.
        # Space: O(h) because the stack only holds the path from root to current node.

        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left

            # pluck the smallest node (last)
            node = stack.pop()
            # one is being consiodered to decrement k
            k -= 1
            # if the nth element == k -> return the value of the node
            if k == 0:
                return node.val

            curr = node.right

        # ====================
        # Optimized recursive DFS with stop condition/variable

        # self.count = k
        # self.found = None

        # def dfs(node):
        #     if not node or self.found is not None:
        #         return

        #     dfs(node.left)
        #     self.count -= 1

        #     if self.count == 0:
        #         self.found = node.val
        #         return

        #     dfs(node.right)

        # dfs(root)
        # return self.found

        # =====================
        # Unoptimized In-order DFS (computes the full tree into a list)

        # def dfs(node):
        #     if not node:
        #         return []

        #     return dfs(node.left) + [node.val] + dfs(node.right)

        # return dfs(root)[k-1]
