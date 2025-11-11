# 🌳 Tree Traversal Companion Sheet

## 🧠 Core Idea

A **traversal** is just an order in which you visit nodes.

You can visit:

the Root first → **Preorder**
the Root in the middle → **Inorder**
the Root last → **Postorder**

or go level by level → **Level-order** (BFS)

## 🌀 1. Recursive Traversals (the clean way)

These are elegant and easy to reason about.
Each call handles one node, then recursively visits its children.

Type	Order	Example (tree)	Code
**Preorder**	Root → Left → Right	[1,2,3] → [1,2,3]
```python
 def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []
```

**Inorder**	Left → Root → Right	BST: [1,2,3] → sorted!
```python 
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
```

**Postorder**	Left → Right → Root	Used for deletions, frees
```python
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
```

## ⚙️ 2. Iterative Traversals (using Stack/Queue)

When recursion isn’t allowed, simulate the call stack manually.

A. **Preorder** (Root → Left → Right)

***Idea***: Stack stores nodes; process node first, then push right then left (so left is visited first).

```python

def preorder_iter(root):
    if not root: return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return res
```

🧩 Stack snapshot example:

Start: [1]
Pop 1 → push right(3), left(2)
Pop 2 → push right(None), left(None)
Pop 3 → done

B. **Inorder** (Left → Root → Right)

***Idea***: Traverse left fully before processing root; right children go on stack later.

```python

def inorder_iter(root):
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res
```

🧩 Stack snapshot:

Push left chain → [1,2,...]
Pop 2 → visit it
Move right → push right child

C. **Postorder** (Left → Right → Root)

***Idea***: Reverse preorder of (Root → Right → Left).

Two common methods:

```python
# Method 1 – Reverse modified preorder

def postorder_iter(root):
    if not root: return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return res[::-1]

#Method 2 – Track visited nodes
# (less intuitive but often used in interviews)

def postorder_iter_2(root):
    stack, res = [], []
    last = None
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            peek = stack[-1]
            if peek.right and last != peek.right:
                root = peek.right
            else:
                res.append(peek.val)
                last = stack.pop()
    return res
```

D. **Level Order** (BFS)

***Idea***: Use a queue, process all nodes level by level.

```python

from collections import deque

def level_order(root):
    if not root: return []
    q = deque([root])
    res = []
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

## 🧩 3. Specialized Traversals

Type	Description	Uses

**Zigzag Level Order**	Alternate left→right then right→left each level	visual BFS variants

**Boundary Traversal**	Visit outer boundary of tree	geometry problems

**Vertical Order / Top View**	Group by column index	coordinate maps

**Morris Traversal**	Inorder without recursion or stack (O(1) space)	memory-limited traversals


## 🧰 4. Stack vs Queue: Mind Model

Traversal Type	Data Structure	Direction	Nature

**DFS (Pre/In/Post)**	Stack	Deep first	Backtracks

**BFS (Level-order)**	Queue	Broad first	Expands evenly

## 🧠 5. Common Traversal Applications

Problem Type	Best Traversal	Reason

**Evaluate expression** tree	Postorder	children before parent

**Serialize tree**	Preorder	root-first encoding

**Build BST** from inorder	Inorder	sorted sequence property

**Find depth**	Postorder	must compute children first

**Find symmetry**	BFS or mirrored DFS	compare mirrored nodes

## 💡 6. Space & Time Complexities

Traversal	Time	Space (avg)	Space (worst)

**Recursive**	O(n)	O(h)	O(n) if skewed

**Iterative DFS**	O(n)	O(h)	O(n) if skewed

**BFS**	O(n)	O(w)	O(n) where w = max width