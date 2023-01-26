from heapq import heappop, heappush
from typing import Dict, List, Set, Tuple


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        area: Dict[int, Set[Tuple[int, int]]] = dict()
        for from_point, to_point, travel_cost in flights:
            if from_point in area:
                mm = area[from_point]
                mm.add((to_point, travel_cost))
            else:
                area[from_point] = {(to_point, travel_cost)}

        # key = city
        # value = dict{jumps, best_cost}
        visited: Dict[int, Dict[int, int]] = dict()

        # (best_cost, city, jumps)
        to_check = []

        heappush(to_check, (0, src, 0))
        visited[src] = {0: 0}

        while len(to_check) > 0:
            # get cheapest route
            current = heappop(to_check)
            if current[1] == dst:
                # dst ist reached
                return current[0]
            if current[2] > k:
                # route are to long
                continue
            if current[1] in area:
                for next_stop, step_cost in area[current[1]]:
                    next_cost = current[0] + step_cost
                    if next_stop not in visited \
                            or current[2] not in visited[next_stop] \
                            or (visited[next_stop][current[2]] > next_cost):
                        visited[next_stop] = {current[2]: next_cost}
                        heappush(to_check, (next_cost, next_stop, current[2]+1))

        return -1

    def findCheapestPrice_1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        area: Dict[int, Dict[int, int]] = dict()
        for from_point, to_point, travel_cost in flights:
            if from_point in area:
                mm = area[from_point]
                mm[to_point] = travel_cost
            else:
                area[from_point] = {to_point: travel_cost}

        visited = dict()
        to_check = []

        heappush(to_check, (0, src, 0))
        visited[src] = {0: 0}

        while len(to_check) > 0:
            current = heappop(to_check)
            if current[1] == dst:
                return current[0]
            if current[2] > k:
                continue
            if current[1] in area:
                for next_stop, step_cost in area[current[1]].items():
                    next_cost = current[0] + step_cost
                    if next_stop not in visited or current[2] not in visited[next_stop] or (visited[next_stop][current[2]] > next_cost):
                        visited[next_stop] = {current[2]: next_cost}
                        heappush(to_check, (next_cost, next_stop, current[2]+1))

        return -1


def do_test(i: int, s, n1, n2, n3, n4, r):
    c = Solution()
    resp = c.findCheapestPrice(s, n1, n2, n3, n4)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1, 700)
    do_test(1, 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200)
    do_test(2, 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500)
    do_test(3, 3, [[0, 1, 1], [0, 2, 3], [1, 0, 2], [1, 2, 10]], 2, 1, 1, -1)
    do_test(4, 3, [[0, 1, 1], [0, 2, 3], [1, 0, 2], [1, 2, 10]], 2, 1, 10, -1)
    do_test(5, 2, [[1, 0, 10]], 1, 0, 1, 10)
