## 🧠 Key Sorting Properties

### 1. **Time Complexity**

How the algorithm’s runtime scales with input size `n`.

| Case             | Meaning                                                               |
| ---------------- | --------------------------------------------------------------------- |
| **Best case**    | When the array is nearly or fully sorted.                             |
| **Average case** | Typical scenario for random data.                                     |
| **Worst case**   | When the array is in the worst possible order (often reverse-sorted). |

---

### 2. **Space Complexity**

How much **extra memory** the algorithm needs beyond the input array.

* **O(1)** = *In-place sort* (modifies the array itself).
* **O(n)** = uses extra arrays or lists.

---

### 3. **Stable**

> Stability means that if two elements have equal keys, they appear in the same **relative order** after sorting.

Example:

```
Input:  [ (A, 2), (B, 1), (C, 2) ]
Stable sort →  [ (B,1), (A,2), (C,2) ]
Unstable sort → [ (B,1), (C,2), (A,2) ]  ← order of A,C flipped
```

Why it matters:

* Important in multi-key sorting (like sorting by last name *then* first name).
* In stable sorts, equal elements preserve their original order.

---

### 4. **Adaptive**

> An **adaptive algorithm** runs faster when the input is partially sorted.

Example:

* If an array is almost sorted, an adaptive sort won’t waste time re-sorting everything.
* **Bubble Sort** and **Insertion Sort** detect sortedness (via swap checks or early exits).

---

### 5. **Number of Writes**

> How many times elements are physically moved (important for systems with costly writes like flash memory).

---

### 6. **Swaps vs Comparisons**

* **Comparisons**: checking if one element is greater/less than another.
* **Swaps**: physically exchanging their positions.
* Algorithms like **Selection Sort** minimize swaps but still do many comparisons.

---

## ⚙️ Algorithm Comparison

| Algorithm          | Time (Best / Avg / Worst) | Space | Stable | Adaptive | # of Writes | Notes                                                                            |
| ------------------ | ------------------------- | ----- | ------ | -------- | ----------- | -------------------------------------------------------------------------------- |
| **Bubble Sort**    | O(n) / O(n²) / O(n²)      | O(1)  | ✅ Yes  | ✅ Yes    | High        | Detects sortedness via `swapped`; simple but inefficient                         |
| **Insertion Sort** | O(n) / O(n²) / O(n²)      | O(1)  | ✅ Yes  | ✅ Yes    | Moderate    | Efficient for small or nearly sorted arrays; used in hybrid sorts (like Timsort) |
| **Selection Sort** | O(n²) / O(n²) / O(n²)     | O(1)  | ❌ No   | ❌ No     | Very Low    | Always scans full remainder to find min; minimizes total swaps                   |

---

## 🔍 Intuitive Summary

| Concept           | Bubble Sort                            | Insertion Sort                           | Selection Sort                                    |
| ----------------- | -------------------------------------- | ---------------------------------------- | ------------------------------------------------- |
| **Core idea**     | Swap adjacent elements if out of order | Insert current element in sorted portion | Select min element and place it in sorted portion |
| **Pass behavior** | Pushes largest to the end each pass    | Builds sorted list left-to-right         | Shrinks unsorted region left-to-right             |
| **Best use case** | Teaching / detecting sortedness        | Small / nearly sorted data               | When minimizing writes is key                     |
| **Stability**     | ✅ Stable                               | ✅ Stable                                 | ❌ Unstable                                        |
| **Adaptivity**    | ✅ Early exit if sorted                 | ✅ Few shifts if nearly sorted            | ❌ Always full passes                              |

---

## 🏁 Concept Recap

* **Stable:** Equal elements keep their original order.
* **Adaptive:** Runs faster on nearly sorted data.
* **In-place:** Sorts using constant space (O(1)).
* **Write-efficient:** Does few element swaps (Selection Sort).
* **Swap-heavy:** Many exchanges (Bubble Sort).
* **Shift-based:** Moves elements without excessive swaps (Insertion Sort).

---
