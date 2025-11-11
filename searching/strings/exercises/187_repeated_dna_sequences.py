from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # RABIN- KARP
        if len(s) < 10:
            return []

        mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
        seen = set()
        repeated = set()
        hash_val = 0

        # Build initial 20-bit hash
        for i in range(10):
            hash_val = (hash_val << 2) | mapping[s[i]]
        seen.add(hash_val)

        mask = (1 << 20) - 1  # Keep last 20 bits
        for i in range(10, len(s)):
            hash_val = ((hash_val << 2) | mapping[s[i]]) & mask
            if hash_val in seen:
                repeated.add(s[i - 9 : i + 1])
            else:
                seen.add(hash_val)

        return list(repeated)

        # RABIN- KARP (not as efficient as version)
        # n = len(s)

        # if n < 10:
        #     return []

        # base = 31
        # mod = 10 ** 9 + 7
        # exp = pow(base, 9, mod)

        # seen = {}
        # res = set()
        # hs = 0

        # for i in range(10):
        #     hs = (hs * base + ord(s[i])) % mod

        # seen[hs] = 0

        # for i in range(n-9):
        #     if i + 10 < n:
        #         hs = (hs - ord(s[i]) * exp) % mod
        #         hs = (hs * base + ord(s[i+10])) % mod
        #         hs = (hs + mod) % mod

        #     if hs in seen:
        #         if s[seen[hs]: seen[hs]+10] == s[i+1:i+11]:
        #             res.add(s[i+1:i+11])

        #     seen[hs] = i + 1

        # return list(res)

        # NAIVE 10-chars window sliding

        # n = len(s)

        # if n < 10:
        #     return []

        # seen = defaultdict(int)

        # for i in range(n - 9):
        #     seen[s[i:i+10]] += 1

        # return [k for k, v in seen.items() if v > 1]
