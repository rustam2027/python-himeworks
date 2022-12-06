class Singleton:

    is_exist = False
    example = 0

    def __new__(cls, *args):
        if not Singleton.is_exist:
            Singleton.is_exist = True
            Singleton.example = object.__new__(cls, *args)

        return Singleton.example


class LRUCache:

    def __init__(self, capacity=16) -> None:
        self.capacity = capacity
        self.len = 0
        self.data = {}
        self.last_call = []

    def put(self, key, value) -> None:
        if self.len + 1 > self.capacity:
            freq = {}
            for i in self.last_call:
                if i not in freq:
                    freq[i] = 1
                else:
                    freq[i] += 1
            while min(freq, key=lambda x: freq[x]) not in self.data:
                freq.pop(min(freq, key=lambda x: freq[x]))

            self.data.pop(min(freq, key=lambda x: freq[x]))
        else:
            self.len += 1
        self.data[key] = value

    def get(self, key):
        if key in self.data:
            if len(self.last_call) > self.capacity:
                self.last_call = self.last_call[1:] + [key]
            else:
                self.last_call = self.last_call + [key]
            return self.data[key]
        else:
            return None

    def _return_all_(self):
        return (self.data, self.last_call)


class OnlyCache(Singleton, LRUCache):
    pass


l1 = OnlyCache()
l2 = OnlyCache()
l1.put(1, "one")
print(l2.get(1))
print(id(l1) == id(l2))
