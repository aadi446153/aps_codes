class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Insert leaf nodes in tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos, value):
        # Update the leaf node
        pos += self.n
        self.tree[pos] = value
        # Update the internal nodes
        i = pos
        while i > 1:
            self.tree[i // 2] = self.tree[i] + self.tree[i ^ 1]
            i //= 2

    def query(self, l, r):
        # Range sum query
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res


# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8]
st = SegmentTree(data)
print(st.query(2, 6))  # Query from index 2 to 5 (3 + 4 + 5 + 6) = 18
st.update(4, 10)  # Update index 4 to 10
print(st.query(2, 6))  # Query from index 2 to 5 (3 + 4 + 10 + 6) = 23
