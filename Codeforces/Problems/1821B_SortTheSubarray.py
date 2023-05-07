t = int(input())

for _ in range(t):
    n = int(input())
    b = [int(x) for x in input().split(" ")]
    a = [int(x) for x in input().split(" ")]

    start = len(b)
    end = 0

    for i in range(len(b)):
        if b[i] != a[i]:
            start = min(start, i)
            end = i

    for i in range(start-1, -1, -1):
        if a[i] > a[i+1]:
            break
        start -= 1
    for i in range(end+1, len(b)):
        if a[i] < a[i-1]:
            break
        end += 1
    print(start+1, end+1)
