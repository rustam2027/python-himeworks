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


fib_numbers = LRUCache()


def fib_optimized(x):
    global fib_numbers

    if fib_numbers.get(x):
        return fib_numbers.get(x)
    if x == 1 or x == 2:
        return 1
    else:
        # print(f"Пришлось считать {x} {fib_numbers._return_all_()}")
        fib_numbers.put(x, fib_optimized(x - 1) + fib_optimized(x - 2))
        return fib_numbers.get(x)


def fib_simple(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib_simple(x - 1) + fib_simple(x - 2)


print(fib_optimized(40))
print(fib_simple(40))
