class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Both are O(n) time and O(n) space. I would choose KMP by default for 459

        # LPS
        n = len(s)

        if n <= 1:
            return False

        lps = [0] * n
        left = 0

        for right in range(1, n):
            while left > 0 and s[left] != s[right]:
                left = lps[left-1]

            if s[left] == s[right]:
                left += 1
                lps[right] = left

        k = lps[-1]

        return k > 0 and n % (n-k) == 0
    
        # Z

        # n = len(s)
        # if n <= 1:
        #     return False

        # Z = [0] * n
        # left = right = 0

        # for i in range(1, n):
        #     if i <= right:
        #         Z[i] = min(right - i + 1, Z[i - left])
        #     while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
        #         Z[i] += 1
        #     if Z[i] >= n - i and n % i == 0:
        #         return True
        #     if i + Z[i] - 1 > right:
        #         left, right = i, i + Z[i] - 1

        # return False

