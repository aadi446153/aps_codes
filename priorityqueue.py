import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0


# Example usage
pq = PriorityQueue()
pq.push(10)
pq.push(1)
pq.push(5)
print(pq.pop())  # 1
print(pq.pop())  # 5
print(pq.pop())  # 10
