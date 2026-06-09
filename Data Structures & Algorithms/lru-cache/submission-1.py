class LRUCache:

    def __init__(self, capacity: int):
        self.LRUCache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            val = self.LRUCache[key]
            del self.LRUCache[key]
            self.LRUCache[key] = val
            return self.LRUCache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            del self.LRUCache[key]
            self.LRUCache[key] = value
            print(self.LRUCache)
        else:
            if len(self.LRUCache) == self.capacity:
                self.LRUCache.popitem(last=False)
            self.LRUCache[key] = value
            print(self.LRUCache)
