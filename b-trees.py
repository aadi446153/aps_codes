class BTreeNode:
    def __init__(self, t):
        self.keys = []
        self.children = []
        self.leaf = True
        self.t = t  # Minimum degree (defines the range for number of keys)

    def split_child(self, i, y):
        t = self.t
        z = BTreeNode(t)
        z.leaf = y.leaf
        z.keys = y.keys[t: (2 * t - 1)]
        if not y.leaf:
            z.children = y.children[t: (2 * t)]
        y.keys = y.keys[0: (t - 1)]
        y.children = y.children[0: t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

    def insert_non_full(self, k):
        if self.leaf:
            i = len(self.keys) - 1
            self.keys.append(None)
            while i >= 0 and k < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            i = len(self.keys) - 1
            while i >= 0 and k < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == (2 * self.t - 1):
                self.split_child(i, self.children[i])
                if k > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(k)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            temp = BTreeNode(self.t)
            self.root = temp
            temp.children.insert(0, root)
            temp.leaf = False
            temp.split_child(0, root)
            temp.insert_non_full(k)
        else:
            root.insert_non_full(k)

    def _inorder(self, node):
        if node:
            for i in range(len(node.keys)):
                self._inorder(node.children[i] if len(node.children) > 0 else None)
                print(node.keys[i], end=' ')
            self._inorder(node.children[len(node.keys)] if len(node.children) > 0 else None)

    def inorder(self):
        self._inorder(self.root)
        print()


# Example usage
btree = BTree(3)
for i in range(10):
    btree.insert(i)
btree.inorder()  # Inorder traversal
