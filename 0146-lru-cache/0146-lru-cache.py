class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.cache:
            # set lru
            if key in self.lru:
                idx = self.lru.index(key)
                self.lru.pop(idx)
                self.lru.append(key)
            else:
                self.lru.append(key)

            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache or len(self.cache) < self.capacity:
            # set lru
            if key in self.lru:
                idx = self.lru.index(key)
                self.lru.pop(idx)
                self.lru.append(key)
            else:
                self.lru.append(key)

            self.cache[key] = value
        else:
            del self.cache[self.lru[0]]
            self.lru.pop(0)
            self.cache[key] = value
            self.lru.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)