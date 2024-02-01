h1, h2, h3, w1, w2, w3 = map(int, input().split())
if h1 + h2 + h3 != w1 + w2 + w3:
    print(0)
    exit()
ans = 0
for a in range(1, h1):
    for b in range(1, h1 - a):
        for c in range(1, h2):
            for d in range(1, h2 - c):
                if (
                    h1 - a - b > 0
                    and h2 - c - d > 0
                    and w1 - a - c > 0
                    and w2 - b - d > 0
                    and h3 + a + b + c + d - w1 - w2 > 0
                ):
                    ans += 1
print(ans)
