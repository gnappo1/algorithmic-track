class Solution:
    def countDistinct(self, s: str) -> int:
        #! IDEAL: Suffix Automaton - O(n) time and space
        
        # DOUBLE HASHING
        # Time about O(n²), space O(n²) for the set of distinct substring

        n = len(s)
        A = [ord(c) - 97 for c in s]

        # double hashing params
        B1, M1 = 911382323, 1_000_000_007
        B2, M2 = 972663749, 1_000_000_009

        # prefix hashes and powers
        H1 = [0] * (n + 1)
        H2 = [0] * (n + 1)
        P1 = [1] * (n + 1)
        P2 = [1] * (n + 1)

        for i, x in enumerate(A, 1):
            H1[i] = (H1[i - 1] * B1 + x) % M1
            H2[i] = (H2[i - 1] * B2 + x) % M2
            P1[i] = (P1[i - 1] * B1) % M1
            P2[i] = (P2[i - 1] * B2) % M2

        def get_hash(l, r):
            # hash of s[l:r]
            h1 = (H1[r] - H1[l] * P1[r - l]) % M1
            h2 = (H2[r] - H2[l] * P2[r - l]) % M2
            return (h1, h2)

        seen = set()
        for k in range(1, n + 1):
            for i in range(0, n - k + 1):
                seen.add((k, *get_hash(i, i + k)))

        return len(seen)

        # SINGLE HASHING
        # O(n³) Time 
        # O(n²) Space

        # n = len(s)

        # output = 0

        # def track_windows(k: int):
        #     # no hashing, simpler

        #     # for i in range(n-k+1):
        #     #     output.add(s[i:i+k])

        #     # hashing to save on slicing and adding to final set
        #     A = [ord(c) - 97 for c in s]
        #     base = 26
        #     mod = 10 ** 9 + 7
        #     power = pow(base, k - 1, mod)

        #     seen = set()
        #     tot = 0
        #     hs = 0
        #     for i in range(k):
        #         hs = (hs * base + A[i]) % mod

        #     seen.add(hs)
        #     tot += 1

        #     for i in range(1, n - k + 1):
        #         hs = (hs - A[i - 1] * power) % mod
        #         hs = (hs * base + A[i+k-1]) % mod
        #         hs = (hs + mod) % mod

        #         if hs not in seen:
        #             seen.add(hs)
        #             tot += 1

        #     return tot

        # for i in range(1, n + 1):
        #     output += track_windows(i)

        # return output
