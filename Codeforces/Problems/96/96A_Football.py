s = input()

resp = False
cur = "-"
cnt = 0
for c in s:
    if c == cur:
        cnt += 1
        if cnt >= 7:
            resp = True
            break
    else:
        cur = c
        cnt = 1


if resp:
    print("YES")
else:
    print("NO")
