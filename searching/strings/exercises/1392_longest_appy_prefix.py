class Solution:
    def longestPrefix(self, s: str) -> str:
        # Time: O(n) to build LPS.
        # Space: O(n) for the LPS array.

        n = len(s)
        lps = [0] * n
        left = 0

        for right in range(1, n):
            while left > 0 and s[left] != s[right]:
                left = lps[left - 1]
            if s[left] == s[right]:
                left += 1
                lps[right] = left

        k = lps[-1]

        return s[:k]

        # Z Algorithm

        # n = len(s)
        # Z = [0] * n
        # left = right = 0

        # for i in range(1, n):
        #     if i <= right:
        #         Z[i] = min(right - i + 1, Z[i - left])
        #     while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
        #         Z[i] += 1
        #     if i + Z[i] - 1 > right:
        #         left, right = i, i + Z[i] - 1

        # for i in range(1, n):
        #     if i + Z[i] == n:
        #         return s[:Z[i]]

        # return ""

        # NAIVE
        # n = len(s)

        # if n <= 1:
        #     return ""

        # prefix = []

        # for i in range(1, n):
        #     prefix.append(s[:i])

        # suffix = []

        # for i in range(n - 1, 0, -1):
        #     suffix.append(s[i:])

        # max_happy = ""

        # for pref in prefix:
        #     if pref in suffix and len(pref) > len(max_happy):
        #         max_happy = pref

        # return max_happy
