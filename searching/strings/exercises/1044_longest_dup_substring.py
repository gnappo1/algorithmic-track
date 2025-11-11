class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # For a fixed length k you slide ~n windows. With one modulus p, the “birthday” chance of at least one collision is about (n²)/(2p).

        #? How to make it safer/faster
        #! Double hashing
            # Keep two hashes (different mods, e.g. 1_000_000_007 and 1_000_000_009, or different bases). Store the pair as the key.
            # Collision chance becomes roughly (n²)/(2 p1 p2) which is astronomically small.
    
        # Time: avg -> O(n log n), worst -> O(n² log n) if there are many collisions or repeated comparisons.
        # Space: O(n) space
        n = len(s)
        # precompute hashes as minor optimization
        # work with a base of 26 (0..25) -> ord("a") is 97
        A = [ord(c) - 97 for c in s]

        low, high = 0, n - 1

        def has_repeat(k: int) -> bool:
            if k == 0:
                return True
            base = 26 #256 since using english lowercase alphabet
            mod = 10**9 + 7
            power = pow(base, k - 1, mod)

            h = 0
            for i in range(k):
                h = (h * base + A[i]) % mod

            seen = {h: [0]}

            for start in range(1, n - k + 1):
                h = (h - A[start - 1] * power) % mod
                h = (h * base + A[start + k - 1]) % mod
                # keep h non-negative
                if h < 0:
                    h += mod

                if h in seen:
                    for prev in seen[h]:
                        if s[prev : prev + k] == s[start : start + k]:
                            return start
                    seen[h].append(start)
                else:
                    seen[h] = [start]
            return False

        start_match = None

        while low < high:
            mid = (low + high + 1) // 2

            match = has_repeat(mid)

            if match:
                start_match = match
                low = mid
            else:
                high = mid - 1

        return s[start_match : start_match + low] if start_match else ""
