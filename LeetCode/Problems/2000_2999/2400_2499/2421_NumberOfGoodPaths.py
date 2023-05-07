from collections import Counter
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        k = dict()
        m = dict()
        for i, n in enumerate(vals):
            el = [None, n, None, None, i]
            m[i] = el
            if n in k:
                k[n].append(el)
            else:
                k[n] = [el]

        k = [(i, e) for i, e in k.items()]
        k.sort(reverse=True)

        # Node 0 is not always the root of the graph. We must first enter all nodes as neighbor nodes.
        # After that we have to decide for a root node.
        for node in edges:
            up_node, down_node = node
            l = m[up_node]
            if l[2] is None:
                l[2] = {down_node, }
            else:
                l[2].add(down_node)
            r = m[down_node]
            if r[2] is None:
                r[2] = {up_node, }
            else:
                r[2].add(up_node)

        # We set the node 0 as the root. To do this, the node must be added as parent to all other nodes and deleted as neighbor.
        # Similarly, all children nodes of the root node must be edited, and their children, ...
        next_childs = [tuple((m[0], None))]

        while len(next_childs):
            a, b = next_childs.pop()
            a[0] = b
            if b is not None:
                a[2].remove(b)
            if a[2] is None:
                continue
            for c in a[2]:
                next_childs.append((m[c], a[4]))

        def get_max_root(a: List[int]) -> int:
            """
            The function runs the maximum possible root node for the current node.
            """
            if a[0] is None:
                return a[4]

            parent = m[a[0]]
            last = a[4]
            while parent[1] <= a[1]:
                last = parent[4]
                if parent[0] is not None:
                    parent = m[parent[0]]
                else:
                    break

            return last

        resp = 0
        while len(k):
            # First, the nodes with the smallest value are processed. So that the nodes can be deleted from the graph.
            check_lists = k.pop()[1]
            count = Counter()

            for x in check_lists:
                count[get_max_root(x)] += 1

            for _, j in count.items():
                resp += j + (j * (j-1)) // 2

            # Delete the processed nodes from the graph. These were the nodes with the smallest values.
            # For the remaining nodes the value is larger in any case, so that the currently processed nodes can be ignored.
            for x in check_lists:
                if x[0] is None or x[2] is None:
                    continue
                childs = x[2]
                parent = m[x[0]]
                if parent[1] > x[1]:
                    continue
                parent[2].remove(x[4])
                for c in childs:
                    m[c][0] = x[0]
                    parent[2].add(c)
                m.pop(x[4])

        return resp

    def numberOfGoodPaths_slow2(self, vals: List[int], edges: List[List[int]]) -> int:

        k = dict()
        m = dict()
        for i, n in enumerate(vals):
            el = [None, n, None, None, i]
            m[i] = el
            if n in k:
                k[n].append(el)
            else:
                k[n] = [el]

        k = [(i, e) for i, e in k.items()]
        k.sort(reverse=True)

        for node in edges:
            up_node, down_node = node
            if up_node > down_node:
                up_node, down_node = down_node, up_node
            u = m[up_node]
            if u[2] is None:
                u[2] = {down_node, }
            else:
                u[2].add(down_node)

            d = m[down_node]
            d[0] = up_node

        def get_deep(a: List[int]) -> int:
            if a[0] is None:
                return 0

            pos = m[a[0]]
            deep = 1
            while pos[0] is not None:
                pos = m[pos[0]]
                deep += 1

            return deep

        def is_ok(a: List[int], b: List[int]) -> bool:
            deep_a = get_deep(a)
            deep_b = get_deep(b)

            pos_a = a
            pos_b = b

            while deep_a > deep_b:
                pos_a = m[pos_a[0]]
                if pos_a[1] > a[1]:
                    return False
                deep_a -= 1

            while deep_b > deep_a:
                pos_b = m[pos_b[0]]
                if pos_b[1] > b[1]:
                    return False
                deep_b -= 1

            while pos_a[4] != pos_b[4]:
                pos_a = m[pos_a[0]]
                if pos_a[1] > a[1]:
                    return False
                pos_b = m[pos_b[0]]
                if pos_b[1] > b[1]:
                    return False

            return True

        resp = len(m)
        while len(k):
            check_lists = k.pop()[1]
            for i in range(len(check_lists)):
                from_point = check_lists[i]
                for j in range(i+1, len(check_lists)):
                    to_point = check_lists[j]
                    if is_ok(from_point, to_point):
                        resp += 1

            for x in check_lists:
                if x[0] is None or x[2] is None:
                    continue
                childs = x[2]
                parent = m[x[0]]
                if parent[1] > x[1]:
                    continue
                parent[2].remove(x[4])
                for c in childs:
                    m[c][0] = x[0]
                    parent[2].add(c)
                m.pop(x[4])

        return resp

    def numberOfGoodPaths_slow(self, vals: List[int], edges: List[List[int]]) -> int:

        k = dict()
        m = dict()
        for i, n in enumerate(vals):
            m[i] = [None, n, None, None, i, None]
            if n in k:
                k[n].append(m[i])
            else:
                k[n] = [m[i]]

        for node in edges:
            up_node, down_node = node
            if up_node > down_node:
                up_node, down_node = down_node, up_node
            u = m[up_node]
            if u[2] is None:
                u[2] = down_node
            else:
                u[3] = down_node

            d = m[down_node]
            d[0] = up_node

        def get_deep(a: List[int]) -> int:
            if a[0] is None:
                return 0
            if a[5] is not None:
                return a[5]

            pos = m[a[0]]
            deep = 1
            while pos[0] is not None:
                pos = m[pos[0]]
                if pos[5] is not None:
                    deep += pos[5]+1
                    break
                deep += 1

            a[5] = deep
            return deep

        def is_ok(a: List[int], b: List[int]) -> bool:
            deep_a = get_deep(a)
            deep_b = get_deep(b)

            pos_a = a
            pos_b = b

            while deep_a > deep_b:
                pos_a = m[pos_a[0]]
                if pos_a[1] > a[1]:
                    return False
                deep_a -= 1

            while deep_b > deep_a:
                pos_b = m[pos_b[0]]
                if pos_b[1] > b[1]:
                    return False
                deep_b -= 1

            while pos_a[4] != pos_b[4]:
                pos_a = m[pos_a[0]]
                if pos_a[1] > a[1]:
                    return False
                pos_b = m[pos_b[0]]
                if pos_b[1] > b[1]:
                    return False

            return True

        resp = len(m)
        while len(k):
            check_lists = k.popitem()[1]
            while len(check_lists):
                from_point = check_lists.pop()
                for to_point in check_lists:
                    if is_ok(from_point, to_point):
                        resp += 1

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.numberOfGoodPaths(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]], 6)
    do_test(1, [1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]], 7)
    do_test(2, [1], [], 1)
    do_test(3, [2, 5, 5, 1, 5, 2, 3, 5, 1, 5], [[0, 1], [2, 1], [3, 2], [3, 4], [3, 5], [5, 6], [1, 7], [8, 4], [9, 7]], 20)
    do_test(4, [2, 1, 1], [[0, 1], [2, 0]], 3)
    do_test(5, [18, 12, 19, 8, 11, 5, 6, 10, 6, 3, 10, 16, 15, 6, 15, 9, 5, 1, 15, 15, 18, 3, 16, 13], [[1, 0], [0, 2], [3, 0], [3, 4], [3, 5], [6, 0], [7, 5], [
            8, 3], [5, 9], [10, 2], [11, 9], [4, 12], [2, 13], [14, 4], [15, 8], [16, 7], [11, 17], [18, 5], [19, 8], [20, 13], [18, 21], [13, 22], [22, 23]], 30)
    do_test(2, [1, 1, 1], [[0, 2], [2, 1]], 6)
