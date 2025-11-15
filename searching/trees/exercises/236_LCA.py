# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # DFS -> signal bubbling up
        # Time Complexity: O(n) in the worst case
        # Space Complexity: O(h), where h is the height of the tree. That’s O(log n) for a balanced tree and O(n) in the worst case.
        if not root:
            return None

        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left
        else:
            return right


        # ==============================
        # BFS
        # queue = deque([(root, [root])])
        # p_path = None
        # q_path = None

        # while queue:
        #     node, path = queue.popleft()

        #     if node is p:
        #         p_path = path

        #     if node is q:
        #         q_path = path

        #     if p_path and q_path:
        #         break

        #     if node.left:
        #         queue.append((node.left, [*path, node.left]))

        #     if node.right:
        #         queue.append((node.right, [*path, node.right]))

        # q_set = set(q_path)
        # for node in reversed(p_path):
        #     if node in q_set: # O(1) time -> membership check in sets
        #         return node
