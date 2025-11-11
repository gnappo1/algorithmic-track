
#! COUNTING SORT
# Properties
# Time: O(n + k)
# Space: O(n+k)
# Stable: ✅
# In-place: ❌

#? Initial Count Array:
# We start by counting how many times each value appears. This count is stored in the count array.
#? Cumulative Count:
# We then transform the count array into a cumulative count. This means that each element in the cumulative count array now represents the total number of elements that are less than or equal to that value.
#? Building the Output Array:
# When we place the elements into the output array, we use the cumulative count to determine the correct position. For each element in the original array, we look at the cumulative count to find out where to place it in the output. Then we decrement the cumulative count for that value so that the next occurrence of the same number will be placed one position earlier.
#? Preserving Stability:
# Because we iterate in reverse order, the relative order of duplicate elements is maintained. This means that if an element appears multiple times, the order in which it appears in the original array is the same in the sorted array.

def counting_sort(arr):
    if not arr:
        return []
    
    min_val, max_val = min(arr), max(arr)
    k = max_val - min_val + 1
    count = [0] * k
    
    for num in arr:
        count[num-min_val] += 1
    
    for i in range(1, k):
        count[i] += count[i-1]
    
    output = [0] * len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        count[arr[i]-min_val] -= 1
        output[count[arr[i]-min_val]] = arr[i]
    
    return output

#==============================
#! RADIX SORT
# Properties
# Time: O(d * (n + b))     # d = number of digits, b = base
# Space: O(n + b)
# Stable: ✅ (if inner sort is stable)
# In-place: ❌

#? Concept:
# Radix Sort works by sorting the numbers digit by digit, starting either from the least
# significant digit (LSD) or the most significant digit (MSD).

#? LSD Approach (Least Significant Digit First):
# We process each digit position starting from the rightmost (ones place)
# to the leftmost (most significant digit).
# In each pass, we use Counting Sort to order the elements based on the current digit,
# while preserving the relative order of elements with the same digit (stability).

#? Digit Extraction:
# For a given digit position determined by exp (1, 10, 100, ...),
# the digit is extracted as: digit = (num // exp) % base
# Example: for num=472 and exp=10 → digit = (472 // 10) % 10 = 7

#? Stable Counting per Digit:
# Each pass performs a stable counting sort on the current digit.
# This guarantees that earlier (less significant) digits remain in the correct order
# when we move to the next (more significant) digit.

#? Handling Negatives:
# Canonical radix sort only works on non-negative integers.
# To handle signed integers, we split the array into negatives and non-negatives:
# - Sort magnitudes of negatives and positives separately using radix sort.
# - Reverse the sorted negatives and negate them.
# - Concatenate negatives before positives.

#? Why Radix Can Beat Comparison Sorts:
# Radix Sort is not based on comparisons between elements.
# When the number of digits (d) is small relative to n, it can achieve near-linear time.
# This makes it especially efficient for large arrays of bounded integers
# (e.g., fixed-length IDs, ZIP codes, or pixel values).

def radix_sort(nums, base=10):
    if len(nums) <= 1:
        return nums[:]
    
    non_neg = [x for x in nums if x >= 0]
    neg = [-x for x in nums if x < 0]
    
    def lsd(nums):
        if not nums:
            return nums
        
        max_v = max(nums)
        exp = 1
        out = [0] * len(nums)
    
        while max_v // exp > 0:
            count = [0] * base
            
            for num in nums:
                digit = (num // exp) % base
                count[digit] += 1
            
            for idx in range(1, base):
                count[idx] += count[idx-1]
            
            
            for i in range(len(nums)-1, -1, -1):
                digit = (nums[i] // exp) % base
                count[digit] -= 1
                out[count[digit]] = nums[i]
            
            exp *= base
            nums, out = out, nums
        
        return nums

    ordered_neg = lsd(neg)
    neg_again = [-x for x in reversed(ordered_neg)]
    
    ordered_non_neg = lsd(non_neg)
    
    return neg_again + ordered_non_neg
    

print(radix_sort([32, 124, 1, -86, 56, -3]))
print(counting_sort([32, 124, 1, -86, 56, -3]))