from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # TIme: O(n⋅log(sum−max))
        # Space = O(1)

        low, high, n = max(nums), sum(nums), len(nums)

        if k == 1:
            return high
        elif n == k:
            return low

        def check_condition(cap):
            groups, acc = 1, 0
            for x in nums:
                if acc + x <= cap:
                    acc += x
                else:
                    groups += 1
                    if groups > k:  # early exit
                        return groups
                    acc = x  # start new group with x
            return groups

        while low < high:
            mid = (low + high) // 2

            if check_condition(mid) > k:
                low = mid + 1
            else:
                high = mid

        return low
