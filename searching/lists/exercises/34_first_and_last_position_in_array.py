from typing import List

class Solution:
    def lower_bound(self, nums, target):
        low, high = 0, len(nums)
        
        while low < high:
            middle = (low + high) // 2

            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle

        return low
    
    def upper_bound(self, nums, target):
        low, high = 0, len(nums)
        
        while low < high:
            middle = (low + high) // 2

            if nums[middle] <= target:
                low = middle + 1
            else:
                high = middle
        
        return low

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.lower_bound(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        second = self.upper_bound(nums, target) - 1
        return [first, second]
        
        
