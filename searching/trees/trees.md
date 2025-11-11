# Trees

## 🌳 Phase 1: Foundations — Understanding Trees

### 1. What a Tree Is

A tree is a **connected acyclic graph**.

It has a **root, edges, and nodes**.

Each node **may have children**; the node pointing to it is its parent.

### 2. Terminology to know by heart

Term	Meaning

**Root**	Topmost node with no parent

**Leaf**	Node with no children

**Edge**	Connection between parent and child

**Height**	Length of the longest path from node to leaf

**Depth**	Distance from root to that node

**Subtree**	A node and all its descendants

**Degree**	Number of children a node has

### 3. Common Tree Types

**Binary Tree**: each node has ≤ 2 children (left, right)

**Full Binary Tree**: every node has 0 or 2 children

**Complete Binary Tree**: all levels are full except possibly last, filled left-to-right

**Perfect Binary Tree**: all internal nodes have 2 children and all leaves are at same depth

**Balanced Binary Tree**: height difference between left and right ≤ 1

**Binary Search Tree** (BST): left < root < right

**N-ary Tree**: each node can have any number of children

### 4. Representing Trees in Python

Typical class structure:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


A binary tree is just a reference to its root node.
You can also represent a tree as:
    Array (Heap-like representation): children at 2*i+1, 2*i+2

Adjacency list (for generic trees/graphs)

### 5. Basic Tree Properties

**Number of edges**: edges = nodes - 1

**Height of tree**: 1 + max(height(left), height(right))

In a perfect binary tree:
    nodes = 2^(h+1) - 1
    leaves = 2^h

***For BSTs: Inorder traversal gives sorted values.***

## 🌱 Phase 2: Traversals (the language of trees)

Every operation on trees is some variant of a traversal — visiting all nodes in a specific order.

### 1. Depth-First Traversals
Type	Order

**Preorder**	Root → Left → Right

**Inorder**	Left → Root → Right

**Postorder**	Left → Right → Root

Recursive examples:

```python
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

```

Iterative versions will use stacks.

### 2. Breadth-First Traversal (BFS) / Level Order

Visit nodes level by level.
Uses a queue.

```python
from collections import deque

def level_order(root):
    if not root: return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

### 3. Typical Traversal Patterns

* Count nodes
* Sum of all values
* Maximum depth
* Minimum/maximum element
* Check if balanced
* Mirror a tree
* Path problems (e.g., path sums, longest path, etc.)

## 🌿 Phase 3: Specialized Trees

### 1. Binary Search Trees (BST)

Left subtree values < root
Right subtree values > root

Common BST operations:

Operation	Description	Time

**Search**	Follow left/right pointers	O(h)

**Insert**	Place new node respecting order	O(h)

**Delete**	Three cases (leaf, one child, two children)	O(h)

***h = height of tree → balanced BST = O(log n)***

### 2. Balanced BST Variants

**AVL Tree**: keeps height difference ≤ 1.

**Red-Black Tree**: maintains balance using color rules.

**Segment Tree / Fenwick Tree**: used for range queries.

**Trie (Prefix Tree)**: for string lookups.

### 3. Heaps

Complete binary tree with heap property:

Min-heap: parent ≤ children
Max-heap: parent ≥ children

Usually represented as array.
Used in Dijkstra, priority queues, sorting (heap sort).

## 🌲 Phase 4: Practical Applications

* Serialization & Deserialization (LeetCode 297)
* Symmetric tree (mirror)
* Diameter of a tree
* Path sum (root-to-leaf paths)
* LCA (Lowest Common Ancestor)
* Balanced vs Unbalanced check
* Convert Sorted Array to BST
* Flatten a binary tree to linked list

## 🧩 Phase 5: Underlying Data Structures

Before you dive into BFS/DFS:

Master Stacks (for iterative DFS, preorder/inorder)

Master Queues (for BFS)

Learn Deques (for optimized level order traversals, zigzag traversals, etc.)