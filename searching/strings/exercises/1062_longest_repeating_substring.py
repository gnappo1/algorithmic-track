class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # Time: O(n log n) on average, since each check is O(n) and we binary search the length.
        # Space: O(n) for hash buckets.

        n = len(s)

        low, high = 0, n - 1

        def has_repeat(k: int) -> bool:
            if k == 0:
                return True
            base = 256
            mod = 10**9 + 7
            power = pow(base, k - 1, mod)

            h = 0
            for i in range(k):
                h = (h * base + ord(s[i])) % mod

            seen = {h: [0]}

            for start in range(1, n - k + 1):
                h = (h - ord(s[start - 1]) * power) % mod
                h = (h * base + ord(s[start + k - 1])) % mod
                # keep h non-negative
                if h < 0:
                    h += mod

                if h in seen:
                    for prev in seen[h]:
                        if s[prev : prev + k] == s[start : start + k]:
                            return True
                    seen[h].append(start)
                else:
                    seen[h] = [start]
            return False

        while low < high:
            mid = (low + high + 1) // 2

            if has_repeat(mid):
                low = mid
            else:
                high = mid - 1

        return low
