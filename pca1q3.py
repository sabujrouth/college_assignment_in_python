# Write a python code to find minimum and maximum elements from array using
# Divide and Conquer approach

print("Sabuj Routh")

def find_min_max(arr, low, high):
    # If there is only one element
    if low == high:
        return arr[low], arr[low]
 
    # If there are two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]
 
    # Divide the array into two halves
    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)
 
    return min(min1, min2), max(max1, max2)
 
# Testing the function
arr = [3, 5, 1, 9, 8, 2, 7]
n = len(arr)
min_val, max_val = find_min_max(arr, 0, n - 1)
print("Minimum element is", min_val)
print("Maximum element is", max_val)