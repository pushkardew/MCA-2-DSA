class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("BST Inorder Traversal:")
bst.inorder(bst.root)
print()

target = 40
result = bst.search(target)
print(f"\nSearch for {target}: {'Found' if result else 'Not Found'}")

target = 99
result = bst.search(target)
print(f"Search for {target}: {'Found' if result else 'Not Found'}")
