from itertools import permutations


cases = int(input())

for _ in range(cases):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n & 1 == 1:
        print(-1)
        continue
    resp = [0] * n
    down = True
    for i in range(n):
        if down:
            down = False
            resp[i] = n-i
        else:
            down = True
            resp[i] = i

    print(*resp)
