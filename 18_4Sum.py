from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        m = {}
        for c in nums:
            old = m.get(c, 0)
            m[c] = old+1

        s = [x for x in m]
        s.sort()

        response = []

        for i_first, first in enumerate(s):
            if first * 4 > target:
                break

            count_first = m[first]
            sec_start = i_first if count_first >= 2 else i_first+1
            for i_second in range(sec_start, len(s)):
                second = s[i_second]

                if second * 3 > target - first:
                    break

                if i_second == i_first and count_first >= 3:
                    th_start = i_first
                elif i_second == i_first and count_first == 2:
                    th_start = i_first + 1
                elif m[second] >= 2:
                    th_start = i_second
                else:
                    th_start = i_second+1

                target_f_s = target - first - second
                for i_third in range(th_start, len(s)):
                    third = s[i_third]

                    if third * 2 > target_f_s:
                        break

                    last = target_f_s - third

                    if last < third:
                        continue

                    is_last = m.get(last, None)
                    if is_last is None:
                        continue

                    count_third = m[third]
                    if last == third:
                        if count_third == 1:
                            continue
                        if third == second:
                            if count_third == 2:
                                continue
                            if second == first and count_third == 3:
                                continue

                    response.append([first, second, third, last])

        return response

    def fourSum_1(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        m = {}
        for c in nums:
            old = m.get(c, 0)
            m[c] = old+1

        s = [x for x in m]
        s.sort()

        response = []

        for i_first, first in enumerate(s):
            sec_start = i_first if m[first] >= 2 else i_first+1
            for i_second in range(sec_start, len(s)):
                second = s[i_second]

                if i_second == i_first and m[first] >= 3:
                    th_start = i_first
                elif i_second == i_first and m[first] == 2:
                    th_start = i_first + 1
                elif m[second] >= 2:
                    th_start = i_second
                else:
                    th_start = i_second+1

                for i_third in range(th_start, len(s)):
                    third = s[i_third]

                    last = target - first - second - third

                    if last < third:
                        continue

                    is_last = m.get(last, None)
                    if is_last is None:
                        continue

                    if last == third and m[third] == 1\
                            or last == third == second and m[third] == 2\
                            or last == third == second == first and m[third] == 3:
                        continue

                    response.append([first, second, third, last])

        return response


def do_test(i: int, s, t, r):
    c = Solution()
    resp = c.fourSum(s, t)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    do_test(1, [2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]])
    do_test(2, [2, 2, 2], 8, [])
    do_test(3, [2, 2, 2, 2, 6], 8, [[2, 2, 2, 2]])
    do_test(4, [2, 2, 2, 6], 8, [])
    do_test(5, [3, -1, -2, -2, -4, 0, 2], 6, [])
    do_test(6, [1, -2, -5, -4, -3, 3, 3, 5], -11, [[-5, -4, -3, 1]])
