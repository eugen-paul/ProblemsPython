from functools import cache
from itertools import product
from typing import Dict, List, Optional, Tuple


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees_s(self, n: int) -> List[Optional[TreeNode]]:
        """sample solution"""
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = [TreeNode(i)]

        for numberOfNodes in range(2, n + 1):
            for start in range(1, n - numberOfNodes + 2):
                end = start + numberOfNodes - 1
                for i in range(start, end + 1):
                    left_subtrees = dp[start][i - 1] if i != start else [None]
                    right_subtrees = dp[i + 1][end] if i != end else [None]

                    for left in left_subtrees:
                        for right in right_subtrees:
                            root = TreeNode(i, left, right)
                            dp[start][end].append(root)

        return dp[1][n]

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def solve(s: Tuple[int]) -> List[Optional[TreeNode]]:
            if len(s) == 0:
                return [None]
            resp = []
            for i in s:
                left = solve(tuple(c for c in s if c < i))
                right = solve(tuple(c for c in s if c > i))
                for l in left:
                    for r in right:
                        resp.append(TreeNode(i, l, r))
            return resp
        return solve(tuple(range(1, n+1)))

    def generateTrees_3(self, n: int) -> List[Optional[TreeNode]]:

        m: Dict[Tuple[int, int], List[Optional[TreeNode]]] = dict()

        def gen_tree(l: int, r: int) -> List[Optional[TreeNode]]:
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]

            if (l, r) in m:
                return m[(l, r)]

            sub_resp = []
            for i in range(l, r+1):
                left = gen_tree(l, i-1)
                right = gen_tree(i+1, r)

                for le, ri in product(left, right):
                    sub_resp.append(TreeNode(i, le, ri))

            m[(l, r)] = sub_resp
            return sub_resp

        return gen_tree(1, n)

    def generateTrees_2(self, n: int) -> List[Optional[TreeNode]]:
        data = [x for x in range(1, n+1)]
        resp = []

        def gen_tree(r: int, left: List[int], right: List[int]) -> List[Optional[TreeNode]]:

            left_trees = []
            for sub_i, sub_n in enumerate(left):
                left_trees.extend(gen_tree(sub_n, left[:sub_i], left[sub_i+1:]))
            if len(left_trees) == 0:
                left_trees.append(None)

            right_trees = []
            for sub_i, sub_n in enumerate(right):
                right_trees.extend(gen_tree(sub_n, right[:sub_i], right[sub_i+1:]))
            if len(right_trees) == 0:
                right_trees.append(None)

            sub_resp = []

            for le, ri in product(left_trees, right_trees):
                sub_resp.append(TreeNode(r, le, ri))

            return sub_resp

        for i in range(1, n+1):
            resp.extend(gen_tree(i, data[:i-1], data[i:]))

        return resp

    def generateTrees_1(self, n: int) -> List[Optional[TreeNode]]:

        data = [x for x in range(1, n+1)]
        resp = []
        m: Dict[Tuple[int, List[int], List[int]], List[TreeNode]] = dict()

        def gen_tree(r: int, left: List[int], right: List[int]) -> List[Optional[TreeNode]]:

            lh = ",".join([str(x) for x in left])
            rh = ",".join([str(x) for x in right])
            if (r, lh, rh) in m:
                return m[(r, lh, rh)]

            left_trees = []
            for sub_i, sub_n in enumerate(left):
                left_trees.extend(gen_tree(sub_n, left[:sub_i], left[sub_i+1:]))
            if len(left_trees) == 0:
                left_trees.append(None)

            right_trees = []
            for sub_i, sub_n in enumerate(right):
                right_trees.extend(gen_tree(sub_n, right[:sub_i], right[sub_i+1:]))
            if len(right_trees) == 0:
                right_trees.append(None)

            sub_resp = []

            for le in left_trees:
                for ri in right_trees:
                    root = TreeNode(r)
                    root.left = le
                    root.right = ri
                    sub_resp.append(root)

            m[(r, lh, rh)] = sub_resp
            return sub_resp

        for i in range(1, n+1):
            resp.extend(gen_tree(i, data[:i-1], data[i:]))

        return resp


def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def do_test(i: int, s, r):
    c = Solution()
    resp = c.generateTrees(s)
    # if resp == r:
    #     print("OK", i)
    # else:
    #     print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, "[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]")
