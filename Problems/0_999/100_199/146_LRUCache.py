from typing import Dict, OrderedDict


class LRUCache:
    cache: OrderedDict[int, int]
    capacity: int

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        resp = self.cache.get(key, -1)
        if resp != -1:
            self.cache.move_to_end(key)
        return resp

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem(False)

        self.cache[key] = value


def do_test(i: int, s, r, n):
    c: LRUCache
    res = True
    for nr, command in enumerate(s):
        if command == "LRUCache":
            c = LRUCache(r[nr][0])
        elif command == "put":
            c.put(r[nr][0], r[nr][1])
        elif command == "get":
            if c.get(r[nr][0]) != n[nr]:
                print("error")
                res = False
    if res:
        print("OK", i)
    else:
        print("ERROR", i)


if __name__ == "__main__":
    do_test(0,
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4]
            )
    do_test(1,
            ["LRUCache", "put", "put", "put", "put", "get", "get"],
            [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]],
            [None, None, None, None, None, -1, 3]
            )
