class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.is_end_of_string = False


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        char = word[index]
        if node is None:
            node = Node(char)
        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 == len(word):
                node.is_end_of_string = True
            else:
                node.middle = self._insert(node.middle, word, index + 1)
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

    def _search(self, node, word, index):
        if node is None:
            return False
        char = word[index]
        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index + 1 == len(word):
                return node.is_end_of_string
            return self._search(node.middle, word, index + 1)


# Example usage
tst = TernarySearchTree()
tst.insert("cat")
tst.insert("car")
tst.insert("bat")
print(tst.search("cat"))  # True
print(tst.search("bat"))  # True
print(tst.search("rat"))  # False
