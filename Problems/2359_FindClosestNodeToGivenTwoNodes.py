from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        way1 = dict()
        way2 = set()

        # Store in a dict all nodes reachable from node 1 and the distance from node 1.
        current = node1
        count = 0
        while current != -1:
            if current not in way1:
                way1[current] = count
                current = edges[current]
                count += 1
            else:
                break

        # Store in a set all nodes that can be reached from node 2 to avoid loops.
        current = node2
        count = 0
        min_distance = 10**6
        min_value = 10**6
        while current != -1:
            # For each node, check whether the node was also reachable from 1.
            if current in way1:
                # If True, then update the result.
                max_d = max(count, way1[current])
                if (min_distance > max_d) or (min_distance == max_d and min_value > current):
                    min_distance = max_d
                    min_value = current
                    if min_distance <= count:
                        # Here the search can be interrupted, because from now on the distance will only be longer.
                        break
            if current not in way2:
                way2.add(current)
                current = edges[current]
                count += 1
            else:
                break

        if min_value == 10**6:
            return -1
        return min_value

    def closestMeetingNode_1(self, edges: List[int], node1: int, node2: int) -> int:
        way1 = dict()
        way2 = dict()

        def init_path(n: int, way: dict):
            current = n
            count = 0
            while current != -1:
                if current not in way:
                    way[current] = count
                    current = edges[current]
                    count += 1
                else:
                    break

        init_path(node1, way1)
        init_path(node2, way2)

        min_distance = 10**6
        min_value = 10**6
        for k, v in way1.items():
            if k in way2:
                max_d = max(v, way2[k])
                if (min_distance > max_d) or (min_distance == max_d and min_value > k):
                    min_distance = max_d
                    min_value = k

        if min_value == 10**6:
            return -1
        return min_value


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.closestMeetingNode(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 2, 3, -1], 0, 1, 2)
    do_test(1, [1, 2, -1], 0, 2, 2)
    do_test(2, [1, 2, -1], 0, 0, 0)
    do_test(3, [5, 3, 1, 0, 2, 4, 5], 3, 2, 3)
