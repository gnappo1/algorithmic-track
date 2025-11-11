## ⚙️ N log N Sorting Algorithms

These algorithms achieve **O(n log n)** time complexity on average, providing a major efficiency improvement over quadratic sorts.

---

## 🧩 Key Concepts

| Property                     | Meaning                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Divide and Conquer**       | Break the array into smaller subarrays, sort them, and combine results.                              |
| **In-place vs Non-in-place** | In-place modifies the array directly (`O(1)` space), while non-in-place needs extra memory (`O(n)`). |
| **Stable vs Unstable**       | Stable algorithms preserve order of equal elements; unstable may not.                                |

---

## 📘 Algorithm Overview

| Algorithm      | Time (Best / Avg / Worst)            | Space    | Stable | In-place | Adaptive | Description                                                                                                      |
| -------------- | ------------------------------------ | -------- | ------ | -------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
| **Merge Sort** | O(n log n) / O(n log n) / O(n log n) | O(n)     | ✅ Yes  | ❌ No     | ❌ No     | Divides array into halves, sorts each recursively, merges them back together. Guaranteed O(n log n) performance. |
| **Quick Sort** | O(n log n) / O(n log n) / O(n²)      | O(log n) | ❌ No   | ✅ Yes    | ❌ No     | Uses a pivot to partition elements smaller/larger, sorts partitions recursively. Average-case fastest.           |
| **Heap Sort**  | O(n log n) / O(n log n) / O(n log n) | O(1)     | ❌ No   | ✅ Yes    | ❌ No     | Builds a max heap, repeatedly extracts the max to the end. Predictable performance, not stable.                  |

---

## 🧠 Merge Sort

**Core idea:** Split → Sort → Merge.

### Process:

1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge sorted halves back into one sorted list.

### Key traits:

* **Stable** and **predictable**.
* **Not in-place** due to additional arrays during merging.
* Ideal for **linked lists** or when memory isn’t a concern.

### Example:

```
[8, 3, 1, 7, 0, 10, 2]
→ [8,3,1] [7,0,10,2]
→ [1,3,8] [0,2,7,10]
→ [0,1,2,3,7,8,10]
```

---

## ⚡ Quick Sort

**Core idea:** Partition around a pivot.

### Process:

1. Choose a pivot (first, last, random, or median element).
2. Partition the array so that all smaller elements go left, larger go right.
3. Recursively sort left and right partitions.

### Variations:

* **Lomuto partition:** simpler but less efficient (single pointer).
* **Hoare partition:** faster (two pointers moving inward).
* **Three-way partition:** handles duplicates efficiently.

### Key traits:

* **In-place** and **cache-efficient**.
* **Unstable**, but usually fastest in practice.
* **Worst case O(n²)** avoided by randomized or median pivot selection.

### Example:

```
Pivot = 7 → [1,3,2,0,7,10,8]
→ Left: [1,3,2,0]  |  Right: [10,8]
→ [0,1,2,3,7,8,10]
```

---

## 🏗️ Heap Sort

**Core idea:** Build a binary heap (complete binary tree) and extract the max repeatedly.

### Process:

1. **Build Max-Heap:** ensures parent ≥ children.
2. **Swap root (max) with last element.**
3. **Reduce heap size** and **heapify** the new root.
4. Repeat until array is sorted.

### Key traits:

* **In-place** and **deterministic** (always O(n log n)).
* **Unstable**, since heap structure doesn’t preserve equal-order elements.
* Preferred for systems requiring guaranteed upper bounds.

### Example:

```
[8, 1, -54, 22, 88, 0, -234]
→ Build heap: [88, 22, 8, 1, 8, 0, -234]
→ Extract max repeatedly → [-234, 0, 1, 8, 22, 88]
```

---

## 🧾 Comparison Summary

| Property               | Merge Sort                      | Quick Sort                          | Heap Sort                             |
| ---------------------- | ------------------------------- | ----------------------------------- | ------------------------------------- |
| **Time Complexity**    | O(n log n)                      | O(n log n) avg / O(n²) worst        | O(n log n)                            |
| **Space Complexity**   | O(n)                            | O(log n)                            | O(1)                                  |
| **Stable**             | ✅                               | ❌                                   | ❌                                     |
| **In-place**           | ❌                               | ✅                                   | ✅                                     |
| **Adaptive**           | ❌                               | ❌                                   | ❌                                     |
| **Deterministic Time** | ✅                               | ❌                                   | ✅                                     |
| **Best Use Case**      | External or linked list sorting | General-purpose, fastest on average | When guaranteed upper bound is needed |

---

## 🏁 Concept Recap

* **Merge Sort:** stable, predictable, space-heavy.
* **Quick Sort:** in-place, fastest average, can degrade.
* **Heap Sort:** in-place, consistent O(n log n), not cache-friendly.

> Together, these three form the **core N log N family** — mastering them means you understand most real-world sorting mechanics used in production compilers and libraries.
