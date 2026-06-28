class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def rotate_left(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1 and data < root.left.data:
        return rotate_right(root)
    if balance < -1 and data > root.right.data:
        return rotate_left(root)
    if balance > 1 and data > root.left.data:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and data < root.right.data:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = insert(root, val)

print("AVL Tree Inorder Traversal:")
inorder(root)
print()
print("Root:", root.data)
