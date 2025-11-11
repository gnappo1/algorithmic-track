class Solution:
    def sumScores(self, s: str) -> int:
        # Time: O(n) —> single pass, each character compared at most twice.
        # Space: O(n) for the Z array.
        
        n = len(s)
        Z = [0] * n
        output = 0

        left = right = 0

        for i in range(1, n):
            if i <= right:
                Z[i] = min(right - i + 1, Z[i - left])
            
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            
            if i + Z[i] - 1 > right:
                left, right = i, i + Z[i] - 1

            output += Z[i]

        return output + n


        