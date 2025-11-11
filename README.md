# 🧠 Algorithms Prep Series

A structured collection of **algorithm practice material**, notes, and code exercises written in **Python**.  
This repo is designed as both a **personal knowledge base** and a **teaching resource**, blending annotated code with markdown explanations and visualizations.

---

## 🚀 Topics Covered

### 🔍 Searching Algorithms
From linear scans to advanced pattern matching:
- **Lists:** two-pointer patterns, binary search, search-on-answer
- **Strings:** Z-algorithm, KMP, Rabin–Karp, suffix automata
- **Trees & Graphs:** BFS, DFS, pathfinding templates

### ⚙️ Sorting Algorithms
Divided by time complexity and concept:
- **Quadratic:** Bubble, Insertion, Selection  
- **N·logN:** Merge, Quick (Lomuto, Hoare, 3-way), Heap  
- **Linear:** Counting, Radix, Bucket

Each algorithm includes:
- Intuitive breakdowns and pseudocode  
- Complexity analysis (time, space, stability, in-place)  
- Practical applications and problem mappings

### 🧩 Practice Exercises
LeetCode-style questions grouped by concept, such as:
- “Search on answer” problems  
- String pattern matching  
- Distinct substring challenges  
- Graph traversal and connected components  

Each file focuses on clean patterns rather than one-off solutions.

---

## 📚 Study Philosophy

This repository follows a **progressive learning pattern**:

1. **Understand the naive idea**  
2. **Optimize step by step** (tracking time & space)  
3. **Generalize the pattern**  
4. **Apply to real-world problems**

Each markdown file reads like a blog post, while `.py` scripts contain runnable, minimal examples with detailed comments.

---

## 🧰 Tools & Environment

- Language: **Python 3.11+**
- Dependencies: none (only `collections`, `math`, `random`)
- Optional: Jupyter Notebook / VSCode setup for step-by-step tracing

---

## 📈 Current Series

1. **Two-pointer Techniques** — windows, opposites, meeting-in-the-middle  
2. **Binary Search Patterns** — classic, rotated, search-on-answer  
3. **Pattern Search in Strings** — Z, KMP, Rabin–Karp  
4. **Graph Traversal** — BFS, DFS, hybrid approaches  
5. **Sorting Series** — quadratic, log-linear, linear

---

## 🧠 Example Usage

```bash
# run a search example
python exercises/searching/lists/search-lists.py

# run sorting tests
python exercises/sorting/nlogn.py
```

## 🪶 Author

[Matteo Piccini](matteopiccini.com) - Full Stack Engineer · Educator · Technical Editor

## 🌟 Contribute

This is a personal learning repo, but feel free to fork and adapt the structure.
If you find optimizations or want to contribute alternative algorithmic patterns, open a PR or leave a comment.

## 🧭 License

MIT License © 2025 Matteo Piccini
Free for educational and personal use.