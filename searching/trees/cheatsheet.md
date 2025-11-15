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


## 7. GENERAL STRATEGIES

### The core recursion template for trees

Almost every binary tree problem with recursion fits this shape:

```python
def dfs(node):
    if node is None:
        return BASE_VALUE   # what makes sense for an empty subtree?

    left  = dfs(node.left)
    right = dfs(node.right)

    # combine info from children + node to build the answer for this subtree
    result = COMBINE(left, right, node)

    return result
```

The game is always:

1. **What should `dfs(node)` return for the subtree rooted at `node`?**
   A number, a boolean, a pair, etc.

2. **What is the base return value when `node` is `None`?**

3. **How do I combine left and right (and maybe node.val) to get the current subtree result?**

That is it.

---

### 1. Height with the template

You already know the formula, so map it to the template.

**Goal**: `dfs(node)` returns the **height** of the subtree.

* Base case: empty subtree has height `0`.
* Recurrence: height is `1 + max(left_height, right_height)`.

```python
def height(root):
    def dfs(node):
        if node is None:
            return 0
        
        left  = dfs(node.left)
        right = dfs(node.right)
        
        return 1 + max(left, right)

    return dfs(root)
```

Map to template:

* `BASE_VALUE` is `0`.
* `COMBINE` is `1 + max(left, right)`.

---

### 2. Diameter with the template

You already know the idea:
Diameter at a node is `left_height + right_height`.
Global diameter is the maximum of these over all nodes.

Here you see a **second pattern**:
Sometimes the function returns one value (height) but you track another value (diameter) in a separate variable.

```python
def diameterOfBinaryTree(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter
        
        if node is None:
            return 0
        
        left_height  = dfs(node.left)
        right_height = dfs(node.right)
        
        # diameter that passes through this node
        diameter = max(diameter, left_height + right_height)
        
        # return height to parent
        return 1 + max(left_height, right_height)

    dfs(root)
    return diameter
```

Pattern:

* `dfs(node)` returns **height**.
* You also update `diameter` using `left_height + right_height`.

So here recursion is used to compute height, and as a side effect you accumulate the best diameter.

---

### 3. Checking if a tree is balanced

Here is the part that often feels tricky, because you need both:

* Is the subtree balanced?
* What is its height?

Instead of two separate passes, return **both values at once**.

**Goal**: `dfs(node)` returns a pair: `(is_balanced, height)`.

```python
def isBalanced(root):
    def dfs(node):
        if node is None:
            # empty subtree is balanced and has height 0
            return True, 0
        
        left_bal,  left_h  = dfs(node.left)
        right_bal, right_h = dfs(node.right)
        
        # current node is balanced if:
        # 1) left is balanced
        # 2) right is balanced
        # 3) heights differ by at most 1
        current_bal = (
            left_bal
            and right_bal
            and abs(left_h - right_h) <= 1
        )
        
        current_h = 1 + max(left_h, right_h)
        
        return current_bal, current_h

    balanced, _ = dfs(root)
    return balanced
```

Template mapping:

* Base case: `True, 0`.
* Combine:

  * `current_h = 1 + max(left_h, right_h)`
  * `current_bal` is a boolean condition using child results.

This is **Pattern 2** in general:
Return multiple pieces of information from the recursion, so each call has everything it needs.

---


## Three big reusable recursion patterns

Let me summarize the three patterns that cover almost every tree problem:

1. **Single value from each subtree**
   Example: height, max depth, sum of values, min value, check BST with bounds, etc.

   ```python
   def dfs(node):
       if not node:
           return BASE

       left  = dfs(node.left)
       right = dfs(node.right)

       return COMBINE(left, right, node)
   ```

2. **Multiple values returned from each subtree**
   Example: isBalanced + height, isBST + min + max, best path sum + max downward path.

   ```python
   def dfs(node):
       if not node:
           return BASE1, BASE2, ...  # tuple

       l1, l2 = dfs(node.left)
       r1, r2 = dfs(node.right)

       # compute current values from children and node
       c1 = ...
       c2 = ...

       return c1, c2
   ```

3. **Return one thing, track another globally**
   Example: diameter, max path sum, number of good nodes, longest univalue path.

   ```python
   def someProperty(root):
       best = INITIAL

       def dfs(node):
           nonlocal best
           if not node:
               return BASE

           left  = dfs(node.left)
           right = dfs(node.right)

           # update best using left, right, node
           best = max(best, SOMETHING(left, right, node))

           return VALUE_FOR_PARENT

       dfs(root)
       return best
   ```

When you see a new problem, ask yourself:

* Can I solve it by returning one clean value per subtree?
* Do I need more than one piece of info per subtree?
* Or is it best to return one thing and maintain a separate global best?

That alone usually tells you which pattern to use.

---