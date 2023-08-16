import bisect
from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

from sortedcontainers import SortedSet

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = Counter()
        h = []
        for i in range(k):
            s[nums[i]] += 1
            heapq.heappush(h, -nums[i])
        resp = [-h[0]]
        for i in range(k, len(nums)):
            s[nums[i]] += 1
            s[nums[i-k]] -= 1
            heapq.heappush(h, -nums[i])
            while s[-h[0]] == 0:
                heapq.heappop(h)
            resp.append(-h[0])
        return resp

    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:
        s = [-x for x in nums[:k]]
        heapq.heapify(s)

        cnt = Counter(nums[:k])

        resp = [-s[0]]

        for i in range(len(nums) - k):
            cnt[nums[i]] -= 1
            if cnt[nums[i]] == 0:
                del cnt[nums[i]]

            cur = nums[i+k]
            cnt[cur] += 1
            heapq.heappush(s, -cur)

            while -s[0] not in cnt:
                heapq.heappop(s)
            resp.append(-s[0])

        return resp

    def maxSlidingWindow_i(self, nums: List[int], k: int) -> List[int]:
        """internet solution:
        https://leetcode.com/problems/sliding-window-maximum/solutions/3231782/239-time-93-21-and-space-81-39-solution-with-step-by-step-explanation/
        """
        # create a deque to hold the indices of the elements in the sliding window
        window = Deque()
        result = []

        # iterate through the array
        for i in range(len(nums)):
            # remove elements from the deque that are outside the window
            while window and window[0] <= i - k:
                window.popleft()

            # remove elements from the deque that are smaller than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            # add the index of the current element to the deque
            window.append(i)

            # add the maximum element in the window to the result list
            if i >= k - 1:
                result.append(nums[window[0]])

        return result

    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:
        s = nums[:k]
        s.sort()

        resp = [s[-1]]

        for i in range(len(nums) - k):
            pos = bisect.bisect_left(s, nums[i])
            s.pop(pos)
            cur = nums[i+k]
            bisect.insort(s, cur)
            resp.append(s[-1])

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxSlidingWindow(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(1, [1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])
    do_test(0, [1], 1, [1])
