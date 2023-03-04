from collections import defaultdict
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    """
    How to count
    input:
    2 2 1 3 4 1 4 2 2 2

    Get first subarray from 0 to X: 
    [2 2 1 3 4]
    
    Count all posible valid subarrays: min(min_position, max_position) + 1
        1 3 4
      2 1 3 4
    2 2 1 3 4

    Get second subarray from 0 to Y (Y > X):
    [2 2 1 3 4 1]
    
    Count all posible valid subarrays: min(min_position, max_position) + 1
            4 1
          3 4 1
        1 3 4 1
      2 1 3 4 1
    2 2 1 3 4 1

    repeat:
              1 4
            4 1 4
          3 4 1 4
        1 3 4 1 4
      2 1 3 4 1 4
    2 2 1 3 4 1 4

    repeat:
              1 4 2 
            4 1 4 2 
          3 4 1 4 2 
        1 3 4 1 4 2 
      2 1 3 4 1 4 2 
    2 2 1 3 4 1 4 2 

    repeat:
              1 4 2 2 
            4 1 4 2 2 
          3 4 1 4 2 2 
        1 3 4 1 4 2 2 
      2 1 3 4 1 4 2 2 
    2 2 1 3 4 1 4 2 2 
    """
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def get_count(sub_nums: List[int]) -> int:
            count = 0
            min_position = max_position = -1

            for i, number in enumerate(sub_nums):
                if number == minK:
                    min_position = i
                if number == maxK:
                    max_position = i

                count += max(0, min(min_position, max_position) + 1)

            return count

        count_min: int = 0
        count_max: int = 0
        sub = Deque()

        resp = 0
        for n in nums:
            if n > maxK or n < minK:
                if count_min > 0 and count_max > 0:
                    resp += get_count(list(sub))
                count_min = 0
                count_max = 0
                sub.clear()
            else:
                sub.append(n)
                if n == minK:
                    count_min += 1
                if n == maxK:
                    count_max += 1
        if count_min > 0 and count_max > 0:
            resp += get_count(list(sub))

        return resp

    def countSubarrays_i(self, nums: List[int], minK: int, maxK: int) -> int:
        """internet solution"""
        # min_position, max_position: the MOST RECENT positions of minK and maxK.
        # left_bound: the MOST RECENT value outside the range [minK, maxK].
        answer = 0
        min_position = max_position = left_bound = -1

        # Iterate over nums, for each number at index i:
        for i, number in enumerate(nums):
            # If the number is outside the range [minK, maxK], update the most recent left_bound.
            if number < minK or number > maxK:
                left_bound = i

            # If the number is minK or maxK, update the most recent position.
            if number == minK:
                min_position = i
            if number == maxK:
                max_position = i

            # The number of valid subarrays equals the number of elements between left_bound and
            # the smaller of the two most recent positions.
            answer += max(0, min(min_position, max_position) - left_bound)

        return answer

    def countSubarrays_x(self, nums: List[int], minK: int, maxK: int) -> int:
        """too slow"""
        def get_count(sub_nums: List[int]) -> int:
            if minK == maxK:
                return (len(sub_nums) * (len(sub_nums) + 1)) // 2

            pos_mm: List[int] = list()
            count_min: int = 0
            count_max: int = 0

            for i, n in enumerate(sub_nums):
                if n == minK or n == maxK:
                    pos_mm.append(i)
                    if n == minK:
                        count_min += 1
                    else:
                        count_max += 1
            visited: Set[Tuple[int, int]] = set()

            to_check: Deque[Tuple[int, int, int, int, int, int]] = Deque()
            to_check.append((0, len(sub_nums)-1, 0, len(pos_mm)-1, count_min, count_max))

            resp = 0

            while to_check:
                l, r, from_pos, to_pos, count_min, count_max = to_check.pop()
                if count_min == 0 or count_max == 0:
                    continue
                if (l, r) in visited:
                    continue
                visited.add((l, r))

                first_pos = pos_mm[from_pos]
                last_pos = pos_mm[to_pos]
                count_left = 1 + first_pos - l
                count_right = r - last_pos + 1
                resp += count_left * count_right

                a_min = count_min-1 if sub_nums[pos_mm[to_pos]] == minK else count_min
                a_max = count_max-1 if sub_nums[pos_mm[to_pos]] == maxK else count_max
                to_check.append((l, last_pos-1, from_pos, to_pos-1, a_min, a_max))

                a_min = count_min-1 if sub_nums[pos_mm[from_pos]] == minK else count_min
                a_max = count_max-1 if sub_nums[pos_mm[from_pos]] == maxK else count_max
                to_check.append((first_pos+1, r, from_pos+1, to_pos, a_min, a_max))

            return resp

        count_min: int = 0
        count_max: int = 0
        sub = Deque()

        resp = 0
        for n in nums:
            if n > maxK or n < minK:
                if count_min > 0 and count_max > 0:
                    resp += get_count(list(sub))
                count_min = 0
                count_max = 0
                sub.clear()
            else:
                sub.append(n)
                if n == minK:
                    count_min += 1
                if n == maxK:
                    count_max += 1
        if count_min > 0 and count_max > 0:
            resp += get_count(list(sub))

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.countSubarrays(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 5, 2, 7, 5], 1, 5, 2)
    do_test(1, [1, 1, 1, 1], 1, 1, 10)
    do_test(2, [1], 1, 1, 1)
    do_test(3, [1, 2, 1, 2, 1], 1, 1, 3)
    do_test(4, [2, 2, 1, 3, 3, 3, 4, 2, 2, 2], 1, 4, 12)
    do_test(5, [2, 2, 1, 3, 4, 1, 4, 2, 2, 2], 1, 4, 32)
    do_test(6, [2, 2, 1, 3, 4, 1, 2, 2, 2], 1, 4, 23)
