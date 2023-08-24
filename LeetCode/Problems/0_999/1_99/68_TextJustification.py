from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        resp = []
        cur = []
        full_len = 0
        for w in words:
            if full_len + len(w) + len(cur) <= maxWidth:
                cur.append(w)
                full_len += len(w)
            else:
                pos = 0
                while full_len < maxWidth:
                    cur[pos] += " "
                    full_len += 1
                    pos = (pos+1) % (max(1, len(cur)-1))
                resp.append("".join(cur))
                cur = [w]
                full_len = len(w)
        resp.append(" ".join(cur) + " "*(maxWidth-full_len-max(0, len(cur)-1)))

        return resp

    def fullJustify_2(self, words: List[str], maxWidth: int) -> List[str]:
        resp = []
        cur = []
        full_len = 0
        for w in words:
            if len(cur) == 0:
                cur.append(w)
                full_len += len(w)
            elif full_len + 1 + len(w) <= maxWidth:
                cur.append(" ")
                cur.append(w)
                full_len += 1+len(w)
            else:
                if len(cur) == 1:
                    resp.append("".join(cur) + " "*(maxWidth-full_len))
                else:
                    pos = 1
                    while full_len < maxWidth:
                        cur[pos] += " "
                        full_len += 1
                        pos = pos+2 if pos+2 < len(cur) else 1
                    resp.append("".join(cur))
                cur = [w]
                full_len = len(w)
        resp.append("".join(cur) + " "*(maxWidth-full_len))

        return resp

    def fullJustify_(self, words: List[str], maxWidth: int) -> List[str]:
        """some ideas from solution"""
        resp = []

        def final_row(r: List[str]) -> str:
            return " ".join(r).ljust(maxWidth)

        def complete_row(r: List[str], w_len: int) -> str:
            if len(r) == 1:
                return final_row(r)

            need_spaces = maxWidth - w_len
            for i in range(need_spaces):
                r[i % (len(r)-1)] += " "

            return "".join(r)

        row = [list(), 0]
        row_len = -1
        for w in words:
            if len(w) <= maxWidth - row_len - 1:
                row[0].append(w)
                row[1] += len(w)
                row_len += len(w) + 1
            else:
                resp.append(complete_row(row[0], row[1]))
                row[0].clear()
                row[0].append(w)
                row[1] = len(w)
                row_len = len(w)
        if len(row) > 0:
            resp.append(final_row(row[0]))

        return resp

    def fullJustify_2(self, words: List[str], maxWidth: int) -> List[str]:
        resp = []

        def final_row(r: List[str]) -> str:
            tmp = " ".join(r)
            tmp = f"{tmp:<{maxWidth}s}"
            return tmp

        def complete_row(r: List[str], w_len: int) -> str:
            if len(r) == 1:
                return final_row(r)

            need_spaces = maxWidth - w_len
            space_len = need_spaces // (len(r)-1)
            sp = ""
            sp = f"{sp:{space_len}s}"
            sp_e = sp + " "
            extra_count = need_spaces - space_len * (len(r)-1)

            resp = ""
            for w in r:
                resp += w
                if need_spaces != 0 and extra_count == 0:
                    resp += sp
                    need_spaces -= len(sp)
                elif need_spaces > 0:
                    resp += sp_e
                    need_spaces -= len(sp_e)
                    extra_count -= 1

            return resp

        row = [list(), 0]
        row_len = -1
        for w in words:
            if len(w) <= maxWidth - row_len - 1:
                row[0].append(w)
                row[1] += len(w)
                row_len += len(w) + 1
            else:
                resp.append(complete_row(row[0], row[1]))
                row[0].clear()
                row[0].append(w)
                row[1] = len(w)
                row_len = len(w)
        if len(row) > 0:
            resp.append(final_row(row[0]))

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.fullJustify(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["This", "is", "an", "example", "of", "text", "justification."], 16, [
        "This    is    an",
        "example  of text",
        "justification.  "
    ])
    do_test(1, ["What", "must", "be", "acknowledgment", "shall", "be"],  16, [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ])
    do_test(2, ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],  20, [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ])
    do_test(3, ["a", "b", "c", "d"],  3, [
        "a b",
        "c d"
    ])
    do_test(4, ["a", "b", "c", "d"],  2, [
        "a ",
        "b ",
        "c ",
        "d "
    ])
    do_test(5, ["a", "b", "c", "d"],  1, [
        "a",
        "b",
        "c",
        "d"
    ])
