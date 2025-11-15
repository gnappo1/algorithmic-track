# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def find_smallest(node):
            while node.left:
                node = node.left
            return node.val

        if not root:
            return None

        if root.val == key:
            if root.left and root.right:
                # iterate over the leftmost branch of the right subtree
                # attach to the leftmost element root.left
                # return root.right
                # start = curr = root.right
                # while curr.left:
                #     curr = curr.left
                # curr.left = root.left
                # return start

                # find inorder successor (min in right subtree)
                # copy successor value into current node
                # delete successor from right subtree
                leftmost = find_smallest(root.right)
                root.val = leftmost
                root.right = self.deleteNode(root.right, leftmost)
            elif root.left or root.right:
                return root.left or root.right
            else:
                return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
