from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # THINK IN TERMS OF SLOPES
        # O(logN) classic binary search
        low, high = 0, len(nums) -1

        while low < high:
            middle = (low + high) // 2

            # two options:
            # the problem guarantees nums[i] != nums[i+1]
            # 1. next element is greater
            if nums[middle] < nums[middle+1]:
                low = middle+1
            else:
            # 2. next element is smaller
            # middle is a potential peak, include it
                high = middle
        
        return low
                


        # O(N) linear search

        # for i in range(0, len(nums)):
        #     if (i<1 or nums[i] > nums[i-1]) and (i>=len(nums)-1 or nums[i] > nums[i+1]):
        #         return i