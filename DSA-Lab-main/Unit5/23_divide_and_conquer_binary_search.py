def binary_search_divide_conquer(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_divide_conquer(arr, target, mid + 1, high)
    else:
        return binary_search_divide_conquer(arr, target, low, mid - 1)

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Sorted Array:", arr)

target = 23
idx = binary_search_divide_conquer(arr, target, 0, len(arr) - 1)
print(f"\nSearching for {target}: {'Found at index ' + str(idx) if idx != -1 else 'Not Found'}")

target = 50
idx = binary_search_divide_conquer(arr, target, 0, len(arr) - 1)
print(f"Searching for {target}: {'Found at index ' + str(idx) if idx != -1 else 'Not Found'}")
