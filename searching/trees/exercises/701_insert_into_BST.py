# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # Time is O(h), where h is the height of the tree, since you follow exactly one path from root to leaf.
        # Space is O(h) due to the call stack.

        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
        # =======================
        # iterative, pointer based DFS

        # if not root:
        #     return TreeNode(val)

        # curr = root

        # while curr:
        #     if val < curr.val:
        #         if not curr.left:
        #             curr.left = TreeNode(val)
        #             break
        #         curr = curr.left
        #     else:
        #         if not curr.right:
        #             curr.right = TreeNode(val)
        #             break
        #         curr = curr.right

        # return root

        # ===============================

        # A bit of overkill with deque since we always go left OR right
        # queue = deque([root])

        # while queue:
        #     node = queue.popleft()

        #     if val < node.val:
        #         if not node.left:
        #             node.left = TreeNode(val)
        #             break
        #         else:
        #             queue.append(node.left)
        #     else:
        #         if not node.right:
        #             node.right = TreeNode(val)
        #             break
        #         else:
        #             queue.append(node.right)

        # return root
