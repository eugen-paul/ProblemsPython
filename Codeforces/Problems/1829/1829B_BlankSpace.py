for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    resp = 0
    cur = 0
    for i in a:
        if i == 0:
            cur += 1
            resp = max(resp, cur)
        else:
            cur = 0
    print(resp)
