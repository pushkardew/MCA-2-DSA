lst = []
lst.append(10)
lst.append(20)
lst.append(30)
print("List after append:", lst)
lst.remove(20)
print("List after remove 20:", lst)
print("List element at index 0:", lst[0])

tpl = (1, 2, 3, 4, 5)
print("\nTuple:", tpl)
print("Tuple element at index 2:", tpl[2])
print("Tuple slicing [1:4]:", tpl[1:4])

st = {1, 2, 3}
st.add(4)
st.discard(2)
print("\nSet after add 4 and discard 2:", st)

dct = {"name": "Alice", "age": 22}
dct["city"] = "Raipur"
del dct["age"]
print("\nDictionary:", dct)
print("Dictionary keys:", list(dct.keys()))
print("Dictionary values:", list(dct.values()))
