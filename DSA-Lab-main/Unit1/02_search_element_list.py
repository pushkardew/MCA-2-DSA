def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

lst = [15, 42, 7, 88, 23, 56]
print("List:", lst)

target = 88
result = linear_search(lst, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")

target = 100
result = linear_search(lst, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
