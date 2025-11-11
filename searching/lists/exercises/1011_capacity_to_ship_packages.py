from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Time: O(n log S) where S is the sum range from max weight to total
        # Space is O(1)
        low, high = max(weights), sum(weights)

        if days == 1:
            return high

        def calc_days_based_on_middle(middle: int):
            elapsed, capacity_acc = 1, 0
            for weight in weights:
                if capacity_acc + weight <= middle:
                    capacity_acc += weight
                else:
                    elapsed += 1
                    capacity_acc = weight

            return elapsed

        while low < high:
            middle = (low + high) // 2

            if calc_days_based_on_middle(middle) > days:
                low = middle + 1
            else:
                high = middle

        return low
