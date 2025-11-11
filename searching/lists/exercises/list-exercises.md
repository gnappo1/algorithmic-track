# Exercises for Lists and Numeric Searches

## 🧩 Binary Search Core & Variants
| #                                                                                                         | Problem                                   | What It Tests | Difficulty |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------- | ---------- |
| [704. Binary Search](https://leetcode.com/problems/binary-search/)                                        | Basic binary search implementation        | 🟢 Easy       |            |
| [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)                       | Lower bound / insertion point             | 🟢 Easy       |            |
| [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)                                | “First True” (binary search on predicate) | 🟢 Easy       |            |
| [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)      | Peak-finding / bitonic structure          | 🟠 Medium     |            |
| [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)       | Modified binary search with rotation      | 🟠 Medium     |            |
| [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | Handle duplicates in rotated search       | 🟠 Medium     |            |

## ⚙️ Boundary & Range Problems (lower/upper bound)
| #                                                                                                                                                     | Problem                          | What It Tests | Difficulty |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------- | ---------- |
| [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Lower and upper bound logic      | 🟠 Medium     |            |
| [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)                                                                           | 2D flattening into binary search | 🟠 Medium     |            |
| [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)                                                                    | Staircase search O(m+n)          | 🟠 Medium     |            |
| [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)                                                                | Binary search on answer pattern  | 🔴 Hard       |            |

## 🚀 Binary Search on Answer (Monotonic Predicate)
| #                                                                                                                               | Problem                                                | What It Tests | Difficulty |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------- | ---------- |
| [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)                                                                             | Integer binary search on numeric domain                | 🟢 Easy       |            |
| [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)                                                | Search on property (x² == n)                           | 🟢 Easy       |            |
| [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)                                                  | Search minimal feasible rate                           | 🟠 Medium     |            |
| [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)         | Search minimal feasible capacity                       | 🟠 Medium     |            |
| [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)     | Search minimal feasible day                            | 🟠 Medium     |            |
| [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | Classic “search smallest value that passes constraint” | 🟠 Medium     |            |
| [1552. Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)                       | Search maximal minimal distance                        | 🔴 Hard       |            |

## 🧮 Special Patterns / Numeric Search Variants
| #                                                                                                                      | Problem                             | What It Tests | Difficulty |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------- | ---------- |
| [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)                                             | Bitonic peak-finding                | 🟠 Medium     |            |
| [1095. Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)                                  | Peak + binary search on both halves | 🔴 Hard       |            |
| [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)       | Find pivot in rotation              | 🟠 Medium     |            |
| [154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | Pivot search with duplicates        | 🔴 Hard       |            |

## 🧠 Meta / Continuous Domain Variants
| #                                                                                                                      | Problem                               | What It Tests | Difficulty |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------- | ---------- |
| [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)                           | Binary search partition technique     | 🔴 Hard       |            |
| [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Binary search on value domain         | 🔴 Hard       |            |
| [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)                                 | Binary search on answer + prefix sums | 🔴 Hard       |            |
