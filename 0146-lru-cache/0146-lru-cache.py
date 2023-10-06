class LRUCache:

    def __init__(self, capacity: int):
        self.dict={}
        self.cap=capacity
    def get(self, key: int) -> int:
        if key in self.dict:
            x=self.dict.pop(key)
            self.dict[key]=x
            return x
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if len(self.dict) == self.cap:
                del self.dict[next(iter(self.dict))]
        self.dict[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)