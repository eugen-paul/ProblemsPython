from typing import List, Set


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        resp = set()
        temp_list = list()

        def gen_seq(pos_to_check, current_element_pos):
            current = nums[current_element_pos]
            for i in range(pos_to_check, len(nums)):
                # We search next digit which is not smaller than current digit.
                next_var = nums[i]
                if next_var < current:
                    continue

                # Call the function recursive. One time with and one time without the found digit.
                temp_list.append(next_var)
                gen_seq(i + 1, i)
                temp_list.pop()
                gen_seq(i + 1, current_element_pos)

                # Further steps are performed recursively. Cancel.
                break

            if len(temp_list) > 1:
                resp.add(tuple(temp_list))

        for i, n in enumerate(nums):
            temp_list.append(n)
            gen_seq(i + 1, i)
            temp_list.pop()

        return [list(x) for x in resp]

    def findSubsequences_web(self, nums: List[int]) -> List[List[int]]:
        curr = [[nums[0]]]
        for x in nums[1:]:
            curr += [y+[x] for y in curr if x >= y[-1]]
            curr += [[x]]
        curr = [tuple(x) for x in curr if len(x) >= 2]
        return list(set(curr))

    def findSubsequences_slow(self, nums: List[int]) -> List[List[int]]:
        resp = set()

        def is_not_decreasing(test_list: list) -> bool:
            current = -101
            for i in test_list:
                if current > i:
                    return False
                current = i
            return True

        for n in range(2**len(nums)):
            l = f"{n:0{len(nums)}b}"
            rrr = list()
            for j, c in enumerate(l):
                if c == '1':
                    rrr.append(nums[j])
            if len(rrr) > 1 and is_not_decreasing(rrr):
                resp.add(tuple(rrr))

        return [list(x) for x in resp]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findSubsequences_web(s)
    resp.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, )
        print("NOK", i, "response", resp)


if __name__ == "__main__":
    do_test(0, [4, 6, 7, 7], [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]])
    do_test(1, [1, 4, 1], [[1, 4], [1, 1]])
    do_test(2, [4, 4, 3, 2, 1], [[4, 4]])
    do_test(3, [4, 5, 6, 1, 2], [[4, 5], [4, 6], [4, 5, 6], [5, 6], [1, 2]])
    do_test(4, [4, 5, 6, 1, 1, 1], [[4, 5], [4, 6], [4, 5, 6], [5, 6], [1, 1], [1, 1, 1]])
    do_test(5, [1, 4, 5, 6, 1, 1, 1], [
        [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 4], [1, 4, 5], [1, 4, 5, 6], [1, 4, 6], [1, 5], [1, 5, 6], [1, 6],
        [4, 5], [4, 5, 6], [4, 6], [5, 6]
    ])
    do_test(6, [1, 4, 1, 4, 1, 4], [
        [1, 1], [1, 1, 1], [1, 1, 1, 4], [1, 1, 4], [1, 1, 4, 4], [1, 4], [1, 4, 4], [1, 4, 4, 4], [4, 4], [4, 4, 4]
    ])
