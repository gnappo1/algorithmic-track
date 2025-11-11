
#! MERGE SORT

def merge_sort(arr: list) -> list: # NLogN time, DIVIDE ET IMPERA, split -> merge -> compare, stable (left_val <= right_val), not in-place
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left:list, right:list) -> list:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:] or right[j:])

    return result

# print(merge_sort([1, 5, 2, 22, -1, 2, 56, -128, 112, -987, 34, 53, -17, 19, 4, 576, -871]))    

#=====================

#! QUICK SORT

def quick_sort(arr:list) -> list:
    # avg case O(nlogn)
    # worst case O(n^2)
    # partitioning is computationally heavy
    # merging is relatively fast
    # in the worst case possible (sorted array last el pivot / reverse sorted array with first pos pivot) we do n partitions and check each element every time -> O(n^2)
    if len(arr) <=1:
        return arr
    
    pivot = arr[-1]
    left = quick_sort([x for x in arr[:-1] if x <= pivot])
    right = quick_sort([x for x in arr[:-1] if x > pivot])
    
    return left + [pivot] + right

# print(quick_sort([1, 5, 2, 22, -1, 2, 56, -128, 112, -987, 34, 53, -17, 19, 4, 576, -871]))    

#! VARIATIONS
#? Lomuto: 
    #* O(N^2) worst time (sorted collection-last pivot), O(NlogN) avg time -> every call we have a left and right, powers of two, N = 2^H -> H = logN max levels -> max stack calls
    #* O(logN) worst time -> every call we have a left and right, powers of two, N = 2^H -> H = logN max levels -> max stack calls
#? Ohare:
    # O(N^2)
#? Dutch Flag / Three Way
    # reduces recursion when there are lots of equal elements.
#? Lomuto with randomized pivot
    # Randomized pivot: swap a random element into the pivot position before partitioning.
    # Median-of-three: choose the median of (first, middle, last) as pivot.
    # Recurse on smaller side first (tail recursion elimination): bounds recursion depth to O(log n).
    
    
def partition_lomuto(arr, low, high):
    # pick the last element as pivot
    # swap elements based on pivot
    #! does fewer swappings than ohare because pivot is at the end
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] < pivot: 
            #! if we do <= then we might swap multiple equal elements from opposite sides and we would lose stability
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort_in_place_lomuto(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high: # there might be nothing to partition otherwise
        p = partition_lomuto(arr, low, high)
        quick_sort_in_place_lomuto(arr, low, p-1) #! DIFFERENCE HERE FROM OHARE: the pivot won't have to move since it's already in the correct position', so we don't include it
        quick_sort_in_place_lomuto(arr, p+1, high)
    
    return arr

def partition_ohare(arr, low, high):
    # pick the center el as pivot
    # loop until you swapped all elements based on pivot -> i >= j
    pivot = arr[(high+low) // 2]
    i, j = low-1, high+1
    while True:
        i += 1
            #! stability is about what causes the swap not the swap itself happening!
            #! here when we find an element that is equal to the pivot we do not increment the counter
            #! we only do a swap if we find a smaller element on the other side
            #! if we do <= then we might swap equal elements from opposite sides and we would lose stability
        while arr[i] < pivot: #! stability
            i += 1
        j -= 1
        while arr[j] > pivot:  #! stability
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_in_place_ohare(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high: # there might be nothing to partition otherwise
        p = partition_ohare(arr, low, high)
        quick_sort_in_place_ohare(arr, low, p) #! DIFFERENCE HERE FROM LOMUTO: the pivot might still have to move since it was more of a separator, so we include it
        quick_sort_in_place_ohare(arr, p+1, high)
    
    return arr

def partition_and_sort_three_way(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low >= high:
        return arr
    
    pivot = arr[low]
    lst, i, gst = low, low+1, high
    
    while i <= gst:
        if arr[i] < pivot:
            arr[i], arr[lst] = arr[lst], arr[i]
            lst+=1
            i+=1
        elif arr[i] > pivot:
            arr[i], arr[gst] = arr[gst], arr[i]
            gst-=1
        else:
            i+=1
    
    partition_and_sort_three_way(arr, low, lst-1)
    partition_and_sort_three_way(arr, lst+1, high)
    return arr
    
def lomuto_with_random_pivot(arr, low=0, high=None):
        # Average time: O(n log n)
        # Worst time: O(n²) (mitigated with randomized/median-of-three/3-way)
        # Space: O(log n) average (recursion)
        # Stable: ❌ (standard quicksort is not stable)
        # In-place: ✅ (in-place variants)
        # When to use: General-purpose sorting on arrays; very fast in practice due to locality/cache-friendliness.
    
    from random import randint
    if high is None:
        high = len(arr) - 1
    
    while low < high:
        idx = randint(low, high)
        arr[high], arr[idx] = arr[idx], arr[high]
        
        p = partition_lomuto(arr, low, high)
        if (p-1-low) < (high-(p+1)):
            lomuto_with_random_pivot(arr, low, p-1)
            low = p+1
        else:
            lomuto_with_random_pivot(arr, p+1, high)
            high = p - 1
    
    return arr


#=====================

#! HEAP SORT

# Time complexity	O(n log n) (all cases)	Each heapify is O(log n); you do ~n of them.
# Space complexity	O(1)	In-place; uses the input array as the heap.
# Stable	❌	Equal elements may swap during heapify.
# Adaptive	❌	Always performs full O(n log n).
# In-place	✅	Only constant extra memory.

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # recursively fix the affected subtree tom restore maxheap property -> subtree because i becomes largest and the next iteration will look down +1, +2

def heap_sort(arr):
    n = len(arr)

    # Build max-heap (bottom-up)
    #! leaf nodes will be at best N//2 in a perfect binary tree
    #! so we only go over the first half of the array, the LAST NON-LEAF NODE
    #! we move backwards from the bottom up to ensure heapification
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for end in range(n - 1, 0, -1):
        #! move largest element at the end of the array
        arr[0], arr[end] = arr[end], arr[0]   # move current max to the end
        #! reduced heap size by 1
        #! heapify the remaining portion of the array
        heapify(arr, end, 0)                  # restore heap property for remaining elements

    return arr



#!========== INVOKE ==================

print(quick_sort_in_place_lomuto([8, 1, -54, 22, 88, 0, -234]))
print(quick_sort_in_place_ohare([8, 1, -54, 22, 88, 0, -234]))
print(partition_and_sort_three_way([8, 1, -54, 22, 88, 0, -234]))
print(lomuto_with_random_pivot([8, 1, -54, 22, 88, 0, -234]))
print(heap_sort([8, 1, -54, 22, 88, 0, -234]))