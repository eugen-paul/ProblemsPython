from typing import Dict, List, Optional, Tuple


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

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
