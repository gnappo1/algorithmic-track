def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        sorted = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = True
        if not sorted:
            return arr
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index=i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index=j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
        
    
# print(bubble_sort([32, 124, 1, -86, 56, -3]))
# print(insertion_sort([32, 124, 1, -86, 56, -3]))
# print(selection_sort([32, 124, 1, -86, 56, -3]))
#!=============END QUADRATIC PRACTICE===========================================

def merge(left, right):
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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def quick_sort(arr): # two scans
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = quick_sort([x for x in arr[:-1] if x <= pivot])
    right = quick_sort([x for x in arr[:-1] if x > pivot])
    
    return left + [pivot] + right

def partition_lomuto(arr, low, high):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i+1
    
def lomuto_quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        p = partition_lomuto(arr, low, high)
        lomuto_quick_sort(arr, low, p-1)
        lomuto_quick_sort(arr, p+1, high)
    
    return arr

def partition_ohare(arr, low, high):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    mid = (low+high) // 2
    pivot = arr[mid]
    
    i, j = low-1, high+1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

    
def ohare_quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        p = partition_ohare(arr, low, high)
        ohare_quick_sort(arr, low, p)
        ohare_quick_sort(arr, p+1, high)
    
    return arr

def random_lomuto_sort(arr, low=0, high=None):
    import random
    if high is None:
        high = len(arr) - 1
    
    while low < high:
        idx = random.randint(low, high)
        arr[idx], arr[high] = arr[high], arr[idx]
        
        p = partition_lomuto(arr, low, high)
        
        if (p - 1 - low) < (high - (p+1)):
            random_lomuto_sort(arr, low, p-1)
            low = p+1
        else:
            random_lomuto_sort(arr, p+1, high)
            high = p-1
    
    return arr

def partition_and_sort_three_way(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low >= high:
        return arr
    
    pivot = arr[low]
    sm, i, lg = low, low+1, high
    while i <= lg:
        if arr[i] < pivot:
            arr[i], arr[sm] = arr[sm], arr[i]
            sm += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[lg] = arr[lg], arr[i]
            lg -= 1
        else:
            i += 1
    
    partition_and_sort_three_way(arr, low, sm)
    partition_and_sort_three_way(arr, sm+1, lg)
    
    return arr
            

def heapify(arr, n, i):
    greatest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[greatest]:
        greatest = left
    if right < n and arr[right] > arr[greatest]:
        greatest = right
    
    if greatest != i:
        arr[greatest], arr[i] = arr[i], arr[greatest]
        heapify(arr, n, greatest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

# print(merge_sort([32, 124, 1, -86, 56, -3]))
# print(quick_sort([32, 124, 1, -86, 56, -3]))
# print(lomuto_quick_sort([32, 124, 1, -86, 56, -3]))
# print(ohare_quick_sort([32, 124, 1, -86, 56, -3]))
# print(random_lomuto_sort([32, 124, 1, -86, 56, -3]))
# print(heap_sort([32, 124, 1, -86, 56, -3]))
# print(partition_and_sort_three_way([32, 124, 1, -86, 56, -3]))

#!=============END LINEALOGARITMIC PRACTICE===========================================

def counting_sort(arr):
    if len(arr) <= 1:
        return arr
    
    low = min(arr)
    high = max(arr)
    
    k = high - low + 1
    count = [0] *  k
    
    for num in arr:
        count[num-low] += 1
    
    for i in range(1, k):
        count[i] += count[i-1]

    output = [0] * len(arr)

    # for num in arr: #! does not preserve order
    #     count[num-low] -= 1
    #     output[count[num-low]] = num
        
    for i in range(len(arr)-1, -1, -1): #! starts bottom-up, therefore preserving relative order 
        # if I find the same element multiple times going bottom-up,
        # that element should stay on the left of previous ones
        # therefore decrement the count so that it gets inserted at a smaller index
        count[arr[i]-low] -= 1
        # insert
        output[count[arr[i]-low]] = arr[i]
        

    return output


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
    
# print(counting_sort([32, 124, 1, -86, 56, -3]))
print(radix_sort([32, 124, 1, -86, 56, -3]))