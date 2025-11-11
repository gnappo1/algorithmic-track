def bubble_sort(arr): # compare pairs, each inner loop ends with the ith greatest value placed at n-i-1
    n = len(arr)
    
    for i in range(n-1): #stop at the one before the last, this way j will have one iteration to go
        swapped = False
        for j in range(n-i-1): # over the remaining elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

print(bubble_sort([1, 5, 2, 22, -1, 2, 56, -128, 112, -987, 34, 53, -17, 19, 4, 576, -871]))    

def selection_sort(arr): # select the smallest on the left at every passage
    n = len(arr)
    
    for i in range(n-1):
        min_pos = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        
        if min_pos != i:
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

print(selection_sort([1, 5, 2, 22, -1, 2, 56, -128, 112, -987, 34, 53, -17, 19, 4, 576, -871]))    

def insertion_sort_adj_swaps(arr): # slide greater values right until in the right place
    
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):   
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    
    return arr
print(insertion_sort([1, 5, 2, 22, -1, 2, 56, -128, 112, -987, 34, 53, -17, 19, 4, 576, -871]))    

