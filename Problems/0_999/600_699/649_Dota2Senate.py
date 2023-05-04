from collections import defaultdict, deque
from functools import cache
from math import inf
from typing import Deque, Generic, List, Dict, Optional, Set, Tuple, Counter, TypeVar

# import sys
# sys.setrecursionlimit(10000)

T = TypeVar('T', bound=str)


class DLLNode(Generic[T]):
    data: T
    next: Optional['DLLNode']

    def __init__(self, data: T):
        self.data = data
        self.next = None


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if len(senate) == 1:
            return "Radiant" if senate[0] == "R" else "Dire"

        first = DLLNode(senate[0])
        first.next = first
        last = first

        for i in range(1, len(senate)):
            nxt = DLLNode(senate[i])
            last.next = nxt
            nxt.next = first
            last = nxt

        lstR = senate.count("R")
        lstD = senate.count("D")
        power = 1
        cur = first.data

        while lstR > 0 and lstD > 0:
            if cur != first.next.data:
                if first.next.data == "R":
                    lstR -= 1
                else:
                    lstD -= 1
                first.next = first.next.next
                power -= 1
            else:
                power += 1
                first = first.next
            if power == 0:
                power = 1
                first = first.next
                cur = first.data

        return "Radiant" if lstD == 0 else "Dire"

    def predictPartyVictory_i(self, senate: str) -> str:
        """sample solution"""

        # Eligible Senators of each party
        r_count = senate.count('R')
        d_count = len(senate) - r_count

        # Floating Ban Count
        d_floating_ban = 0
        r_floating_ban = 0

        # Queue of Senators
        q = deque(senate)

        # While any party has eligible Senators
        while r_count and d_count:

            # Pop the senator with turn
            curr = q.popleft()

            # If eligible, float the ban on the other party, enqueue again.
            # If not, decrement the floating ban and count of the party.
            if curr == 'D':
                if d_floating_ban:
                    d_floating_ban -= 1
                    d_count -= 1
                else:
                    r_floating_ban += 1
                    q.append('D')
            else:
                if r_floating_ban:
                    r_floating_ban -= 1
                    r_count -= 1
                else:
                    d_floating_ban += 1
                    q.append('R')

        # Return the party with eligible Senators
        return 'Radiant' if r_count else 'Dire'


def do_test(i: int, s, r):
    c = Solution()
    resp = c.predictPartyVictory(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "RD", "Radiant")
    do_test(1, "RDD", "Dire")
    do_test(2, "DDR", "Dire")
    do_test(3, "DDRRR", "Dire")
    do_test(4, "RRDRDDRDRRDDDDDRDRDR", "Radiant")
