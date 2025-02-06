def binary_search_recursive(arr, target, low, high):
    
    ######## 1) We need base case ##########
    if low > high:
        return -1 
    ######################################## 

    mid = (low + high) // 2 

    ######## 2) We have three possible cases ##########
    # 1. if we reach target
    if arr[mid] == target:
        return mid

    # 2. if target is smaller than the value located in 'mid'
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)

    # 3. if target is larger than the value located in 'mid'
    else:
        return binary_search_recursive(arr, target, low, mid + 1)

# Use case
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.") 