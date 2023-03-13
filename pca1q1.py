# Write a python code to find minimum and maximum elements from array

print("Sabuj Routh")

def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for val in arr:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return min_val, max_val

# Example usage
arr = [5, 3, 8, 1, 9, 2]
min_val, max_val = find_min_max(arr)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")