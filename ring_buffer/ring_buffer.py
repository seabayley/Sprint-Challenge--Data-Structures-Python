class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None for i in range(capacity)]
        self.capacity = capacity
        self.oldest_index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.pop(0)
            self.storage.append(item)
        else:
            self.storage[self.oldest_index] = item
            if self.oldest_index == len(self.storage)-1:
                self.oldest_index = 0
            else:
                self.oldest_index += 1

    def get(self):
        return [i for i in self.storage if i is not None]
