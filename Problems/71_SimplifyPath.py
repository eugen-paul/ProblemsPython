from typing import Deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        resp_path = Deque()

        for p in path.split("/"):
            if len(p) == 0 or p == ".":
                continue
            if p == "..":
                if len(resp_path) > 0:
                    resp_path.pop()
                continue
            resp_path.append(p)

        if len(resp_path) == 0:
            return "/"

        return "/" + "/".join(resp_path)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.simplifyPath(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "/home/", "/home")
    do_test(1, "/../", "/")
    do_test(2, "/home//foo/", "/home/foo")
