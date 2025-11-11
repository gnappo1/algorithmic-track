## KMP (prefix function / LPS)

• 28. Implement strStr? Easy → Classic KMP search
• 459. Repeated Substring Pattern Easy → Use LPS border check
• 686. Repeated String Match Medium → KMP over repeated text
• 796. Rotate String Easy → KMP on s+s to find goal
• 214. Shortest Palindrome Hard → KMP on s + ‘#’ + reverse(s)
• 1392. Longest Happy Prefix Hard → LPS last value
• 1668. Maximum Repeating Substring Easy → KMP over repeated pattern

## Z algorithm

• 28. Implement strStr? Easy → Do it again with Z on p + ‘#’ + s
• 459. Repeated Substring Pattern Easy → Z border idea
• 1316. Distinct Echo Substrings Medium → Z to detect equal halves
• 2223. Sum of Scores of Built Strings Hard → Pure Z over the string
• 1392. Longest Happy Prefix Hard → Can also be solved with Z
• Bonus drill Build Z from scratch and solve “find all occurrences” with p + ‘#’ + s

## Rabin–Karp rolling hash

• 28. Implement strStr? Easy → RK baseline
• 187. Repeated DNA Sequences Medium → Rolling 10-char windows
• 1062. Longest Repeating Substring Medium → Binary search length + RK
• 1044. Longest Duplicate Substring Hard → Binary search length + RK
• 1698. Number of Distinct Substrings in a String Medium → Rolling hash set
• 2156. Find Substring With Given Hash Value Medium → Reverse rolling hash
• 1923. Longest Common Subpath Hard → Multi-set RK with binary search

## Multi-pattern

* Aho–Corasick for multiple words search (e.g., censorship filters)

## sliding window cousins

* 76 Minimum Window Substring
* 438 Find All Anagrams in a String
* 567 Permutation in String