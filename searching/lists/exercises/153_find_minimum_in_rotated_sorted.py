from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low < high:
            middle = (low+high) // 2

            # if the middle is smaller than high -> we had a rotation -> move up and ook on the right wjere smaller elements are
            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                #otherwise no rotation, so look on the left since the right is sorted
                high = middle
                
        
        return nums[low]