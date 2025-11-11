class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Time: Still ≈ O(m + n) across k..k+2 tries.
        # Space: O(m + (k+2)·n) because you materialize the big string(s).
        # Pros: Clear and fast enough.
        # Cons: Extra allocations and memory spikes.
        
        # n, m = len(a), len(b)

        # def build_lps(word):
        #     n = len(word)
        #     lps = [0] * n
        #     i = 0
        #     for j in range(1, n):
        #         while i > 0 and word[i] != word[j]:
        #             i = lps[i - 1]
        #         if word[i] == word[j]:
        #             i += 1
        #             lps[j] = i
        #     return lps

        # k = (m + n - 1) // n
        # lps = build_lps(b)
        # text = a * k

        # for times in range(k, k + 3):
        #     p = len(text)

        #     i = j = 0  # over text and b
        #     while i < p:
        #         if text[i] == b[j]:
        #             i += 1
        #             j += 1
        #             if j == m:
        #                 return times
        #         else:
        #             if j > 0:
        #                 j = lps[j - 1]
        #             else:
        #                 i += 1
        #     text += a

        # return -1
    
    
    #! Delegate to Python
    # Time: ≈ O(m + n) in practice (Two-Way is linear), often faster than Python-level KMP due to C speed.
    # Space: O((k+2)·n) for the biggest concatenated string.
    # Pros: Shortest code, usually fastest in CPython for typical sizes.
    # Cons: Builds large strings; can blow memory or GC time if m is huge.
        n, m = len(a), len(b)
        k = (m + n - 1) // n
        
        for time in range(k, k+3):
            if b in a*time:
                return time
        
        return -1