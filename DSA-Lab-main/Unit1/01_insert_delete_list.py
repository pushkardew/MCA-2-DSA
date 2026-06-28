def insert_element(lst, position, element):
    lst.insert(position, element)
    return lst

def delete_element(lst, position):
    if position < 0 or position >= len(lst):
        raise IndexError("Position out of range")
    lst.pop(position)
    return lst

lst = [10, 20, 30, 40, 50]
print("Original List:", lst)

lst = insert_element(lst, 2, 99)
print("After inserting 99 at position 2:", lst)

lst = delete_element(lst, 4)
print("After deleting element at position 4:", lst)
