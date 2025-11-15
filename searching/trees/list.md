1. Trees (Foundations)

Focus on:
* DFS (recursive and iterative)
* BFS (level-order traversal)
* Binary Search Tree (BST) properties
* Inorder, Preorder, Postorder
* Height, Diameter, Symmetry, Balance
* Lowest Common Ancestor
* Path problems (sum paths, longest path, etc.)
* Serialization/deserialization (LeetCode 297)

Key problems to start:
* 94. Binary Tree Inorder Traversal
* 102. Binary Tree Level Order Traversal
* 104. Maximum Depth of Binary Tree
* 110. Balanced Binary Tree
* 543. Diameter of Binary Tree
* 236. Lowest Common Ancestor
* 124. Binary Tree Maximum Path Sum
* 297. Serialize and Deserialize Binary Tree

---

# **LEVEL 1: Core recursion muscles**

Finish these so they feel automatic:

1. **Max depth (104)**
2. **Diameter (543)**
3. **Balanced tree (110)**
4. **Invert a binary tree (226)**
5. **Same tree / Symmetric tree (100)**
6. **Count nodes (222)** (simple DFS)

These are *pattern-building*. After these, recursion will feel like Lego bricks.

---

# **LEVEL 2: Understanding recursion + state (the classic interview ones)**

These introduce combining recursion with extra logic:

1. **Path Sum** I (root→leaf equals target)
2. **Path Sum II** (return all paths)
3. **Sum of Left Leaves**
4. **Min Depth**
5. **Lowest Common Ancestor (LCA)** — the real unlock

LCA is the big one.
It uses the recursion template but teaches you how recursion passes *signals* up the tree.

If you understand LCA, you will suddenly “see” tree solutions before writing them.

---

# **LEVEL 3: Binary Search Tree mechanics**

BSTs introduce ordered constraints. This is a new mental model.

Do these next:

1. **Validate BST** (inorder or min/max)
2. **Insert in BST**
3. **Search in BST**
4. **Delete from BST** (the real tricky one)
5. **Kth smallest in BST** (inorder traversal)

BSTs teach you how **structure** gives you shortcuts.

---

# **LEVEL 4: Path-based and global-maximum problems**

These are the ones people consider “hard” until they learn the pattern.
But after you master diameter + LCA, this becomes easier mentally.

1. **Binary Tree Maximum Path Sum (Hard)**
   This uses the *diameter template* but vertical (node.val + one branch).

2. **Longest Univalue Path**

3. **Good Nodes**

4. **Pseudo-palindromic paths**

5. **Average of Levels** (mix BFS and DFS patterns)

These problems teach you how to:

* return one thing from DFS
* track another globally
* handle tree paths that “reset” at nodes

---

# **LEVEL 5: Tree construction**

This is the “final boss” category for classic trees.

If you can solve:

1. **Construct tree from preorder + inorder**
2. **Construct tree from inorder + postorder**
3. **Serialize / Deserialize Binary Tree**

…you are completely done with tree fundamentals.
These force you to think:

* which subtrees belong where
* how recursion splits the problem
* how indexes/arrays reflect structural relationships


---

# **LEVEL 6: Level-order mastery (BFS)**

After your DFS shapes are solid, go deeper into BFS:

* **Zigzag level order**
* **Right side view**
* **Level averages**
* **Nodes per row**
* **Check completeness of a binary tree**

This gives you the other half of the toolkit.
Every tree problem uses either:

* DFS with recursive templates
* BFS with queues

After this, you have both.

---

# **LEVEL 7: Combo problems (graph + tree, DP + tree)**

You only do this later, once the fundamentals are “muscle memory.”

Examples:

* **Time to infect binary tree**
* **Distance K in BST or BT**
* **Binary tree cameras**
* **House robber III** (tree DP)
* **Google style LCA with parents + visited sets**

This is where you show senior-level reasoning and structure.

---

