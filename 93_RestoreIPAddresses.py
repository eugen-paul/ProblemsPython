from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        resp = list()

        def gen_ip(current: List[str], sub_s: str):
            if len(current) == 4 and len(sub_s) != 0:
                return

            if len(current) == 4:
                resp.append(".".join(current.copy()))
                return

            if len(sub_s) == 0:
                return

            for i in range(1, 4):
                if i > len(sub_s):
                    break
                current_sub = sub_s[:i]
                if len(current_sub) > 1 and current_sub[0] == '0':
                    break
                if int(current_sub) > 255:
                    break

                current.append(current_sub)
                gen_ip(current, sub_s[i:])
                current.pop()

        gen_ip(list(), s)

        return resp

    def restoreIpAddresses_2(self, s: str) -> List[str]:
        resp = list()

        def gen_ip(current: List[str], pos: int):
            if len(current) == 3:
                last = s[pos:]
                if len(last) > 1 and last[0] == '0':
                    return
                if int(last) <= 255:
                    resp.append(".".join(current.copy() + [last]))
                return

            for i in range(pos+1, len(s) - (3 - len(current))+1):
                current_dig = s[pos:i]
                if len(current_dig) > 1 and current_dig[0] == '0':
                    break
                if int(current_dig) > 255:
                    break

                current.append(current_dig)
                gen_ip(current, i)
                current.pop()

        gen_ip(list(), 0)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.restoreIpAddresses(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "25525511135", ["255.255.11.135", "255.255.111.35"])
    do_test(1, "0000", ["0.0.0.0"])
    do_test(2, "101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])
