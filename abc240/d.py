from collections import deque

N = int(input())
a = list(map(int, input().split()))
count = 0
d = deque([(0, 0)])
for i in range(N):
    now = d.pop()
    count -= now[1]
    if now[0] == a[i]:
        next = (now[0], now[1] + 1)
        if next[0] != next[1]:
            d.append(next)
            count += next[1]
    else:
        d.append(now)
        count += now[1]
        d.append((a[i], 1))
        count += 1
    print(count)
