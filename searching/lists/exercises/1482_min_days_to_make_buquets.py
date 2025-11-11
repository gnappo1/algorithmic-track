from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Time: O(n log R), where R is max(bloomDay) - min(bloomDay) + 1.
        # Space: O(1).
        n = len(bloomDay)

        if m * k > n:
            return -1

        if k == 1:
            return sorted(bloomDay)[m - 1]

        def count_bloomed_after_d_days(d):
            streak = 0
            groups = 0

            for bloom in bloomDay:
                if bloom <= d:
                    streak += 1
                    if streak == k:
                        groups += 1
                        if groups == m:  # if we're done, early exit
                            return groups
                        streak = 0
                else:
                    streak = 0

            return groups

        low, high = min(bloomDay), max(bloomDay)

        while low < high:
            middle = (low + high) // 2

            if count_bloomed_after_d_days(middle) < m:
                low = middle + 1
            else:
                high = middle

        return low
