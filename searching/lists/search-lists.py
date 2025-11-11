
#! AGENDA

#! LINEAR SEARCH
# Properties
# Time: O(n)
# Space: O(1)
# Needs sorted input: ❌

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    
    return -1

#! BINARY SEARCH (iterative)
# Properties
# Time: O(log n)
# Space: O(1)
# Needs sorted input: ✅

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low+high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
        
    return -1

#? Float version:
def binary_search_float(low, high, ok, eps=1e-6):
    """Return x with precision eps such that ok(x) just turns True."""
    while high - low > eps:
        mid = (low + high) / 2
        if ok(mid):
            high = mid
        else:
            low = mid
    return low

#! LOWER_BOUND / UPPER_BOUND
# Properties
# Time: O(log n)
# Space: O(1)
# Needs sorted input: ✅
# lower_bound → first index i with arr[i] >= x
# upper_bound → first index i with arr[i] >  x

def lower_bound(arr, target): # escluso il numero
    low, high = 0, len(arr)
    
    while low < high:
        mid = (low+high) // 2
        
        if arr[mid] < target:
            low = mid+1
        else:
            high = mid
        
    return low

def upper_bound(arr, target): # incluso il numero
    low, high = 0, len(arr)
    
    while low < high:
        mid = (low+high) // 2
        
        if arr[mid] <= target:
            low = mid+1
        else:
            high = mid
        
    return low

print(linear_search([1, 2, 3, 5, 6, 7], 4))
print(binary_search([1, 2, 3, 5, 6, 7], 4))
print(lower_bound([1, 2, 3, 4, 5, 6, 7], 4))
print(upper_bound([1, 2, 3, 4, 5, 6, 7], 4))

#! BINARY SEARCH ON ANSWER
# Properties
# Time: O(log R) where R = high - low over the search domain
# Space: O(1)
# Stable: n/a
# In-place: ✅

#? Concept:
# We are not searching for an array element. We search for the smallest (or largest)
# numeric value x that satisfies a monotonic condition.
# If condition(x) is True, then it is True for all larger x (or all smaller x), so the
# boolean answers form a prefix or suffix of True values. That lets us binary search x.

#? Typical uses:
# 1) Integer sqrt: smallest x with x*x >= n
# 2) Minimum capacity or speed to finish within D days or H hours
# 3) Minimize the maximum of something under constraints
# 4) Find minimal time or cost where feasibility is monotone

def binary_search_on_answer(low, high, condition):

    while low < high:
        middle = (low + high) // 2
        if condition(middle):
            high = middle
        else:
            low = middle + 1
    
    return low

# Search in Rotated Sorted Array

# Peak-finding / Bitonic search