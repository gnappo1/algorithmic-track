# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # RECURSIVE DFS WITH BUILT-IN STACK
        # COMPLEXITIES
        # TIME: O(MIN(N, M)) where N is the nodes in p and M the nodes in q
        # SPACE: O(H) -> logN in a perfect tree but N is a skewed tree
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # RECURSIVE DFS WITH BUILT-IN STACK - REFACTOR
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # return p is q

        # ITERATIVE DFS WITH CUSTOM STACK
        # TIME: O(MIN(N, M)) where N is the nodes in p and M the nodes in q
        # SPACE: O(H) -> logN in a perfect tree but N is a skewed tree
        # stack = deque([(p, q)])

        # while stack:
        #     a, b = stack.pop()

        #     if not a and not b:
        #         continue
        #     if not a or not b or a.val != b.val:
        #         return False

        #     stack.append((a.left, b.left))
        #     stack.append((a.right, b.right))

        # return True

        # ITERATIVE BFS WITH CUSTOM QUEUE
        # TIME: O(MIN(N, M)) where N is the nodes in p and M the nodes in q
        # SPACE: O(W) -> the last level will have 2^h nodes, which is roughly N/2 -> O(N) in a complete tree

        # queue = deque([(p, q)])

        # while queue:
        #     a, b = queue.popleft()

        #     if not a and not b:
        #         continue
        #     if not a or not b or a.val != b.val:
        #         return False

        #     queue.append((a.left, b.left))
        #     queue.append((a.right, b.right))

        # return True
