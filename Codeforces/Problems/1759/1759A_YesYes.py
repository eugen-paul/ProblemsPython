s: str = input()

lines = int(s)

for _ in range(lines):
    w: str = input()
    last = ""
    ok = True
    for c in w:
        if c not in "Yes" \
                or (last == "Y" and c != "e")\
                or (last == "e" and c != "s") \
                or (last == "s" and c != "Y"):
            ok = False
            break
        last = c

    if ok:
        print("YES")
    else:
        print("NO")
