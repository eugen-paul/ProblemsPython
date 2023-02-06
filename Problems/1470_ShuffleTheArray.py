from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        resp = []
        for c in zip(nums[:len(nums) // 2], nums[len(nums) // 2:]):
            resp.append(c[0])
            resp.append(c[1])

        return resp

    def shuffle_1(self, nums: List[int], n: int) -> List[int]:
        resp = [0] * 2 * n
        for i in range(len(nums)):
            if i % 2 == 0:
                resp[i] = nums[i // 2]
            else:
                resp[i] = nums[i // 2 + n]

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.shuffle(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7])
    do_test(1, [1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1])
    do_test(2, [1, 1, 2, 2], 2, [1, 2, 1, 2])
