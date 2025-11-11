class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Z Algo
        n, m = len(haystack), len(needle)

        if not m or n < m:
            return -1

        def build_z(s):
            n = len(s)
            Z = [0] * n

            L = R = 0

            for i in range(1, n):
                if i <= R:
                    Z[i] = min(Z[i - L], R - i + 1)
                while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                    Z[i] += 1
                if i + Z[i] - 1 > R:
                    L, R = i, i + Z[i] - 1

            return Z

        combo = needle + "#" + haystack
        o = len(combo)
        Z = build_z(combo)

        for i in range(m + 1, o):
            if Z[i] == m:
                return i - m - 1

        return -1

        # ===================
        # KMP
        # n, m = len(haystack), len(needle)

        # if not m or n < m:
        #     return -1

        # def build_lps(word):
        #     n = len(word)
        #     lps = [0] * n
        #     i = 0
        #     for j in range(1, n):
        #         while i > 0 and word[i] != word[j]:
        #             i = lps[i-1]
        #         if word[i] == word[j]:
        #             i += 1
        #             lps[j] = i
        #     return lps

        # lps = build_lps(needle)
        # i = j = 0 # over haystack and needle

        # while i < n:
        #     if haystack[i] == needle[j]:
        #         i += 1
        #         j +=1
        #         if j == m:
        #             return i - j
        #     else:
        #         if j > 0:
        #             j = lps[j-1]
        #         else:
        #             i += 1

        # return -1


# ================
# RABIN-KARP
# n, m = len(haystack), len(needle)

# if not m or n < m:
#     return -1

# base = 26
# mod = 10 ** 9 + 7
# power = pow(base, m-1, mod)

# hh = 0
# hn = 0

# for i in range(m):
#     hn = (hn * base + ord(needle[i])) % mod
#     hh = (hh * base + ord(haystack[i])) % mod

# for i in range(n - m + 1):
#     if hh == hn:
#         if haystack[i:i+m] == needle:
#             return i
#     if i < n - m:
#         hh = (hh - ord(haystack[i]) * power) % mod
#         hh = (hh * base + ord(haystack[i+m])) % mod
#         hh = (hh + mod) % mod

# return -1


# ====================
# TOTAL WORST CASE: O((n−m+1)⋅m)≈O(n⋅m)
# Time Complexity:The outer loop runs at most: (𝑙𝑒𝑛(ℎ𝑎𝑦𝑠𝑡𝑎𝑐𝑘)−𝑙𝑒𝑛(𝑛𝑒𝑒𝑑𝑙𝑒)+1)≈𝑂(𝑛−𝑚+1)
# Slice haystack[i:i+m] and compare it to needle:
#     -Slicing haystack[i:i+m] creates a substring → O(m).
#     -Comparing to needle is also O(m).
# Thus, each iteration costs O(m) in the worst case.


# Total Worst Case: O(m)
# Space Complexity: The slicing haystack[i:i+m] allocates a new substring of length m each time. This creates a transient O(m) space usage per iteration. Overall auxiliary space is O(1) if we disregard the transient slices (Python discards them after each loop).
# i = 0
# while i < len(haystack) - len(needle) + 1:
#     if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
#         return i
#     i+=1

# return -1
