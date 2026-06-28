import array

arr = array.array('i', [10, 20, 30, 40, 50])
print("One-Dimensional Array:", arr)

print("Traversal:")
for element in arr:
    print(element, end=" ")
print()

arr.append(60)
print("After append 60:", arr)

arr.remove(30)
print("After remove 30:", arr)

print("Element at index 2:", arr[2])
print("Length of array:", len(arr))
