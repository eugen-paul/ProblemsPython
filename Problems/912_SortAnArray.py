from typing import Deque, List, Dict, Tuple, Counter


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        buf = Deque()
        to_check: Deque[Tuple[bool, int, int]] = Deque()
        to_check.append((True, 0, len(nums)-1))

        while to_check:
            status, l, r = to_check.pop()
            if r-l < 1:
                continue

            if status:
                m = (r+l)//2
                to_check.append((False, l, r))
                to_check.append((True, l, m))
                to_check.append((True, m+1, r))
            else:
                m = (r+l)//2
                p2 = m+1
                for i in range(l, m + 1):
                    while p2 <= r and nums[i] > nums[p2]:
                        buf.append(nums[p2])
                        p2 += 1
                    buf.append(nums[i])

                for i in range(p2, r + 1):
                    buf.append(nums[i])

                nums[l:r+1] = buf
                buf.clear()

        return nums

    def sortArray_2(self, nums: List[int]) -> List[int]:
        buf = Deque()

        def sub(l: int, r: int):
            if r-l < 1:
                return
            m = (r+l)//2
            sub(l, m)
            sub(m+1, r)
            p2 = m+1

            for i in range(l, m + 1):
                while p2 <= r and nums[i] > nums[p2]:
                    buf.append(nums[p2])
                    p2 += 1
                buf.append(nums[i])

            for i in range(p2, r + 1):
                buf.append(nums[i])

            for i, n in enumerate(buf):
                nums[l+i] = n
            buf.clear()

        sub(0, len(nums)-1)
        return nums

    def sortArray_1(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        l = self.sortArray(nums[:len(nums) // 2])
        r = self.sortArray(nums[len(nums) // 2:])
        p2 = 0

        resp = []
        for i in range(len(l)):
            while p2 < len(r) and l[i] > r[p2]:
                resp.append(r[p2])
                p2 += 1
            resp.append(l[i])
        for i in range(p2, len(r)):
            resp.append(r[i])

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.sortArray(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [5, 2, 3, 1], [1, 2, 3, 5])
    do_test(1, [5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5])
    do_test(2, [1], [1])
