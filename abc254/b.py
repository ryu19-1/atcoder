N = int(input())
dp = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(i+1):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
for i in range(N):
    print(dp[i].join(' '))