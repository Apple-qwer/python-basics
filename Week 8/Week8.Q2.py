def sum_recursion(arr):
    if not arr: 
        return 0 
    return arr[0] + sum_recursion(arr[1:])

# Test
print(sum_recursion([1, 2, 3, 4, 5]))  # Output: 15