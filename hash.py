class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        for idx, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                self.table[hash_key][idx] = (key, value)
                return
        self.table[hash_key].append((key, value))

    def search(self, key):
        hash_key = self._hash_function(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key {key} not found in hash table")

    def delete(self, key):
        hash_key = self._hash_function(key)
        for idx, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                del self.table[hash_key][idx]
                return
        raise KeyError(f"Key {key} not found in hash table")

# Example usage:
hash_table = HashTable(10)
hash_table.insert(5, "Apple")
hash_table.insert(10, "Banana")
hash_table.insert(15, "Cherry")

print(hash_table.search(10))  # Output: Banana

hash_table.delete(10)
try:
    print(hash_table.search(10))
except KeyError as e:
    print(e)  # Output: Key 10 not found in hash table
