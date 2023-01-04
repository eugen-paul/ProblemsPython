from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = {}
        for current in nums:
            counter = m.get(current, 0)
            m[current] = counter+1

        k = [key for key in m]
        k.sort()

        response = []

        if m.get(0, 0) >= 3:
            response.append([0, 0, 0])

        for i, first in enumerate(k):
            # The list k is sorted. The sum of three positive numbers cannot be 0.
            if first >= 0:
                break

            if m[first] >= 2:
                sum_of_2 = first * 2
                if 0-sum_of_2 in m:
                    response.append([first, first, 0-sum_of_2])

            for j in range(i+1, len(k)):
                second = k[j]
                sum_of_2 = first + second
                third = 0-sum_of_2
                # The searched number is smaller than second number
                # last number can't be the first number
                if second > third:
                    break
                third_counter = m.get(third, None)
                # if     last number is in m
                #    and last number not second number (exception: second number comes twice)
                if third_counter is not None and ((second == third and third_counter > 1) or second < third):
                    response.append([first, second, third])

        return response

    def threeSum_alt(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        m = {}
        for current in nums:
            counter = m.get(current, 0)
            m[current] = counter+1

        k = [key for key in m]

        response = []

        if m.get(0, 0) >= 3:
            response.append([0, 0, 0])

        for i, current in enumerate(k):
            if current >= 0:
                break

            left = i if m[current] >= 2 else i+1
            right = len(k)-1

            while left <= right:
                if left == right and (m[k[left]] == 1 or (m[k[left]] == 2 and left == i)):
                    break
                s = current + k[left] + k[right]
                if s == 0:
                    response.append([current, k[left], k[right]])
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1

        return response

    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        m = {}
        for current in nums:
            counter = m.get(current, 0)
            m[current] = counter+1

        k = [key for key in m]
        k.sort()

        response = []

        for i, current in enumerate(k):
            if current > 0:
                break
            if current == 0:
                if m[current] >= 3:
                    response.append([0, 0, 0])
                break
            else:
                if m[current] >= 2:
                    s = current * 2
                    if m.get(0-s, None) is not None:
                        response.append([current, current, 0-s])

                for j in range(i+1, len(k)):
                    s = current + k[j]
                    t = m.get(0-s, None)
                    if t is not None and 0-s != current and k[j] <= 0-s and t > 1:
                        response.append([current, k[j], 0-s])
                    if t is not None and 0-s != current and k[j] < 0-s and t == 1:
                        response.append([current, k[j], 0-s])

        return response


def do_test(i: int, s, r):
    c = Solution()
    resp = c.threeSum(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    do_test(1, [0, 1, 1], [])
    do_test(2, [0, 0, 0], [[0, 0, 0]])
    do_test(3, [1, 1, -2], [[-2, 1, 1]])
    do_test(4, [-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])
    do_test(5, [-10, 0, 5, 5], [[-10, 5, 5]])
    do_test(6, [-10, 0, 5, 5, 4, 6], [[-10, 4, 6], [-10, 5, 5]])
    do_test(7, [-10, 0, 5, 4, 6], [[-10, 4, 6]])
    do_test(8, [-2, -1, -1, -1, -1, -1, 1, 1, 1, 1], [[-2, 1, 1]])
