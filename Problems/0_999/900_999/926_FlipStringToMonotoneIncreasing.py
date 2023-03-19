class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        swaps_to_zero = 0
        swaps_to_one = s.count("0")

        resp = swaps_to_one
        for x in s:
            if x == "0":
                swaps_to_one -= 1
            else:
                swaps_to_zero += 1
                
            resp = min(resp, swaps_to_one + swaps_to_zero)

        return resp

    def minFlipsMonoIncr_2(self, s: str) -> int:
        resp = 10**6

        to_zero = []
        to_one = []

        sum_zero = 0
        sum_one = 0

        for x in s:
            if x == "0":
                to_zero.append(0)
                to_one.append(1)
                sum_one += 1
            else:
                to_zero.append(1)
                to_one.append(0)

        for i in range(len(s)):
            resp = min(resp, sum_zero + sum_one)
            sum_zero += to_zero[i]
            sum_one -= to_one[i]

        resp = min(resp, sum_zero + sum_one)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minFlipsMonoIncr(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "00110", 1)
    do_test(1, "010110", 2)
    do_test(2, "00011000", 2)
    do_test(3, "111111", 0)
    do_test(4, "000000", 0)
    do_test(5, "011111", 0)
    do_test(6, "1001111", 1)
