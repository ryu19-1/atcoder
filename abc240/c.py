N, X = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * 10005
dp[0] = 1
for i in range(N):
    nextdp = [0] * 10005
    for j in range(10005):
        if dp[j] == 1:
            nextdp[j + ab[i][0]] = 1
            nextdp[j + ab[i][1]] = 1
    dp = nextdp
print("Yes") if dp[X] == 1 else print("No")
