class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # Outer loop runs over starts i with early break when m < 2.
        # For each i, building Z on length m = n - i costs O(m), then scanning l up to m//2 costs O(m).
        # Total time is O(n²).
        # Extra space is O(n) for the Z array, plus the set of distinct substrings.
        n = len(text)
        results = set()

        for i in range(n):
            s = text[i:]
            m = len(s)

            if m < 2:
                break

            Z = [0] * m
            left = right = 0

            for k in range(1, m):
                if k <= right:
                    Z[k] = min(right - k + 1, Z[k - left])

                while k + Z[k] < m and s[Z[k]] == s[k + Z[k]]:
                    Z[k] += 1

                if k + Z[k] - 1 > right:
                    left, right = k, k + Z[k] - 1

            for l in range(1, (m // 2) + 1):
                if l <= Z[l]:
                    results.add(s[: l * 2])

        return len(results)
