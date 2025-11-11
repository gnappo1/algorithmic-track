from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return -1
        
        low, high = 0, len(nums)-1

        while low <= high:
            middle = (low+high) // 2

            if nums[middle] == target:
                return True

            if nums[low] == nums[middle] == nums[high]:
                low += 1
                high -= 1
                continue
            
            if nums[low] <= nums[middle]:
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
        
        return False