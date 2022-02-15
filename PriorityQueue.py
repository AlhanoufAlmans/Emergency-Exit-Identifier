import heapq


class Node:
    def __init__(self, cost, key, location, steps):
        self.cost = cost
        self.key = key
        self.location = location
        self.steps = steps


class PriorityQueue:
    def __init__(self):
        self._data = []
        self._index = 0

    def push(self , cost, key , steps, priority, location):
        heapq.heappush(self._data, (priority, Node(cost, key, location, steps)))
        self._index += 1

    def peek(self):
        if self.size() > 0:
            return self._data[0]
        else:
            return -1

    def pop(self):
        if len(self._data) > 0:
            return heapq.heappop(self._data)
        else:
            return None

    def Print(self):
        for i in range(len(self._data)):
            item = self._data[i][-1]
            if len(self._data) > 0:
                print('Data: ', item.data, 'Freq: ', item.frequency, 'Right: ', item.right, 'Left: ', item.left)
            else:
                print('Data: ', item.data, 'Freq: ', item.frequency)

    def size(self):
        return len(self._data)
