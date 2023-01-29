import heapq
from typing import Counter, Dict, List, Tuple


class RNode:
    def __init__(self, val: int, r: int, next=None, prev=None, cx=None):
        self.val = val
        self.r = r
        self.next = next
        self.prev = prev
        self.cx = cx


class CNode:
    def __init__(self, cnt: int, next=None, prev=None, first: RNode = None):
        self.cnt = cnt
        self.next = next
        self.prev = prev
        self.first = first
        self.last = first


class LFUCache:

    # key -> (value, last_round)
    data: Dict[int, Tuple[int, RNode]]
    c_list: CNode
    capa: int
    r: int

    def __init__(self, capacity: int):
        self.data = dict()
        self.capa = capacity
        self.r = 0
        self.c_list = None

    def get(self, key: int) -> int:
        if self.capa == 0:
            return -1

        self.r += 1

        if key not in self.data:
            return -1

        old_value = self.data[key]
        old_rx = old_value[1]
        old_cx = old_value[1].cx
        old_cx_removed = False
        if old_rx.prev != None and old_rx.next != None:
            old_rx.prev.next = old_rx.next
            old_rx.next.prev = old_rx.prev
        elif old_rx.prev != None and old_rx.next == None:
            old_rx.prev.next = None
            old_rx.cx.last = old_rx.prev
        elif old_rx.prev == None and old_rx.next != None:
            old_rx.next.prev = None
            old_rx.cx.first = old_rx.next
        else:
            old_cx_removed = True
            if old_cx.prev != None and old_cx.next != None:
                old_cx.prev.next = old_cx.next
                old_cx.next.prev = old_cx.prev
            elif old_cx.prev != None and old_cx.next == None:
                old_cx.prev.next = None
            elif old_cx.prev == None and old_cx.next != None:
                old_cx.next.prev = None
                self.c_list = old_cx.next
            else:
                self.c_list = None

        old_rx.r = self.r
        target_cx = old_cx.next
        if target_cx == None:
            new_cx = CNode(old_cx.cnt+1, first=old_rx)
            old_rx.cx = new_cx
            old_rx.prev = None
            old_rx.next = None
            if not old_cx_removed:
                old_cx.next = new_cx
                new_cx.prev = old_cx
            elif self.c_list == None:
                self.c_list = new_cx
            else:
                old_cx.prev.next = new_cx
                new_cx.prev = old_cx.prev
        elif target_cx.cnt == old_cx.cnt+1:
            target_cx.last.next = old_rx
            old_rx.prev = target_cx.last
            old_rx.next = None
            old_rx.cx = target_cx
            target_cx.last = old_rx
        else:
            new_cx = CNode(old_cx.cnt+1, first=old_rx)
            old_rx.cx = new_cx
            old_rx.prev = None
            old_rx.next = None
            if not old_cx_removed:
                old_cx.next = new_cx
                new_cx.prev = old_cx
                new_cx.next = target_cx
                target_cx.prev = new_cx
            elif self.c_list == target_cx:
                self.c_list = new_cx
                new_cx.next = target_cx
                target_cx.prev = new_cx
            else:
                old_cx.prev.next = new_cx
                new_cx.prev = old_cx.prev
                new_cx.next = target_cx
                target_cx.prev = new_cx

        return old_value[0]

    def put(self, key: int, value: int) -> None:
        if self.capa == 0:
            return
        self.r += 1

        if len(self.data) < self.capa or key in self.data:
            if key not in self.data:
                rx = RNode(key, self.r)
                if self.c_list == None:
                    self.c_list = CNode(1, first=rx)
                    rx.cx = self.c_list
                elif self.c_list.cnt == 1:
                    self.c_list.last.next = rx
                    rx.prev = self.c_list.last
                    self.c_list.last = rx
                    rx.cx = self.c_list
                else:
                    f_list = CNode(1, first=rx)
                    f_list.next = self.c_list
                    self.c_list.prev = f_list
                    self.c_list = f_list
                    rx.cx = self.c_list
                self.data[key] = (value, rx)
            else:
                old_value = self.data[key]
                old_rx = old_value[1]
                old_cx = old_value[1].cx
                old_cx_removed = False
                if old_rx.prev != None and old_rx.next != None:
                    old_rx.prev.next = old_rx.next
                    old_rx.next.prev = old_rx.prev
                elif old_rx.prev != None and old_rx.next == None:
                    old_rx.prev.next = None
                    old_rx.cx.last = old_rx.prev
                elif old_rx.prev == None and old_rx.next != None:
                    old_rx.next.prev = None
                    old_rx.cx.first = old_rx.next
                else:
                    old_cx_removed = True
                    if old_cx.prev != None and old_cx.next != None:
                        old_cx.prev.next = old_cx.next
                        old_cx.next.prev = old_cx.prev
                    elif old_cx.prev != None and old_cx.next == None:
                        old_cx.prev.next = None
                    elif old_cx.prev == None and old_cx.next != None:
                        old_cx.next.prev = None
                        self.c_list = old_cx.next
                    else:
                        self.c_list = None

                old_rx.r = self.r
                target_cx = old_cx.next
                if target_cx == None:
                    new_cx = CNode(old_cx.cnt+1, first=old_rx)
                    old_rx.cx = new_cx
                    old_rx.prev = None
                    old_rx.next = None
                    if not old_cx_removed:
                        old_cx.next = new_cx
                        new_cx.prev = old_cx
                    elif self.c_list == None:
                        self.c_list = new_cx
                    else:
                        old_cx.prev.next = new_cx
                        new_cx.prev = old_cx.prev
                elif target_cx.cnt == old_cx.cnt+1:
                    target_cx.last.next = old_rx
                    old_rx.prev = target_cx.last
                    old_rx.next = None
                    old_rx.cx = target_cx
                    target_cx.last = old_rx
                else:
                    new_cx = CNode(old_cx.cnt+1, first=old_rx)
                    old_rx.cx = new_cx
                    old_rx.prev = None
                    old_rx.next = None
                    if not old_cx_removed:
                        old_cx.next = new_cx
                        new_cx.prev = old_cx
                        new_cx.next = target_cx
                        target_cx.prev = new_cx
                    elif self.c_list == target_cx:
                        self.c_list = new_cx
                        new_cx.next = target_cx
                        target_cx.prev = new_cx
                    else:
                        old_cx.prev.next = new_cx
                        new_cx.prev = old_cx.prev
                        new_cx.next = target_cx
                        target_cx.prev = new_cx
                self.data[key] = (value, old_rx)
        else:
            # remove last
            to_remove = self.c_list.first
            self.data.pop(to_remove.val)
            if to_remove.next == None:
                self.c_list = to_remove.cx.next
                if self.c_list is not None:
                    self.c_list.prev = None
            else:
                to_remove.next.prev = None
                to_remove.cx.first = to_remove.next

            rx = RNode(key, self.r)
            if self.c_list == None:
                self.c_list = CNode(1, first=rx)
                rx.cx = self.c_list
            elif self.c_list.cnt == 1:
                self.c_list.last.next = rx
                rx.prev = self.c_list.last
                self.c_list.last = rx
                rx.cx = self.c_list
            else:
                f_list = CNode(1, first=rx)
                f_list.next = self.c_list
                self.c_list.prev = f_list
                self.c_list = f_list
                rx.cx = self.c_list
            self.data[key] = (value, rx)
        pass


class LFUCache_1:
    """TO SLOW"""
    data: Dict[int, Tuple[int, int]]
    key_cnt: Counter
    cnt_to_key: Dict[int, List[int]]
    capa: int
    r: int

    def __init__(self, capacity: int):
        self.data = dict()
        self.key_cnt = Counter()
        self.capa = capacity
        self.r = 0

    def get(self, key: int) -> int:
        if self.capa == 0:
            return -1

        self.r += 1
        resp = self.data.get(key, (-1, -1))
        if resp[0] != -1:
            self.key_cnt[key] += 1
            self.data[key] = (resp[0], self.r)
        return resp[0]

    def put(self, key: int, value: int) -> None:
        if self.capa == 0:
            return

        self.r += 1
        if len(self.data) < self.capa or key in self.data:
            if key in self.data:
                self.key_cnt[key] += 1
            else:
                self.key_cnt[key] = 1
            self.data[key] = (value, self.r)
        else:
            vals = reversed(self.key_cnt.most_common())
            value_to_remove = 1_000_000
            round_to_remove = 1_000_000
            min_cnt = None
            for k, v in vals:
                if min_cnt != None and min_cnt != v:
                    break
                if round_to_remove > self.data[k][1]:
                    value_to_remove = k
                    round_to_remove = self.data[k][1]
                    min_cnt = v
            self.data.pop(value_to_remove)
            self.key_cnt.pop(value_to_remove)
            self.data[key] = (value, self.r)
            self.key_cnt[key] = 1
        pass


def do_test(i: int, s, n, r):
    c = LFUCache(n[0][0])

    for op in range(1, len(s)):
        if s[op] == "put":
            c.put(n[op][0], n[op][1])
        elif s[op] == "get":
            resp = c.get(n[op][0])
            if resp == r[op]:
                print("OK", i)
            else:
                print("NOK", i, "expected", r[op], "response", resp)


if __name__ == "__main__":
    do_test(0, ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, 3, None, -1, 3, 4])
    do_test(1, ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
            [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]],
            [None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,14,None,None,18,None,None,11,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,-1,None,None,None,20,None,None,None,29,18,18,None,None,None,None,20,None,None,None,None,None,None,None])
