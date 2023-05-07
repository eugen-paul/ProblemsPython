from typing import Deque


class BrowserHistory:

    hist: Deque[str]
    forw: Deque[str]

    def __init__(self, homepage: str):
        self.hist = Deque()
        self.hist.append(homepage)
        self.forw = Deque()

    def visit(self, url: str) -> None:
        self.hist.append(url)
        self.forw = Deque()

    def back(self, steps: int) -> str:
        st = min(len(self.hist)-1, steps)
        site = self.hist[-1]
        for _ in range(st):
            self.forw.append(self.hist.pop())
            site = self.hist[-1]
        return site

    def forward(self, steps: int) -> str:
        st = min(len(self.forw), steps)
        site = self.hist[-1]
        for _ in range(st):
            site = self.forw.pop()
            self.hist.append(site)
        return site


def do_test(i: int, s, r, n):
    c: BrowserHistory
    res = True
    for nr, command in enumerate(s):
        if command == "BrowserHistory":
            c = BrowserHistory(r[nr][0])
        elif command == "visit":
            c.visit(r[nr][0])
        elif command == "back":
            if c.back(r[nr][0]) != n[nr]:
                print("error")
                res = False
        elif command == "forward":
            if c.forward(r[nr][0]) != n[nr]:
                print("error")
                res = False
        else:
            print("UNKNOWN Parameter")
    if res:
        print("OK", i)
    else:
        print("ERROR", i)


if __name__ == "__main__":
    do_test(0,
            ["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"],
            [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]],
            [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com", "google.com", "leetcode.com"]
            )
