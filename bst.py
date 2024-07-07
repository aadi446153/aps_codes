class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val)
            self._inorder(root.right)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)


# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.inorder()  # Inorder traversal
print(bst.search(60) is not None)  # True
print(bst.search(25) is not None)  # False
