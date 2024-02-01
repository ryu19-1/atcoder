N = int(input())
A = list(map(int, input().split()))
P = 0
dp = [0 for _ in range(4)]
for i in range(N):
    dp[0] += 1
    nextdp = dp.copy()
    for j in range(4):
        if dp[j] == 1:
            nextdp[j] -= 1
            if j + A[i] < 4:
                nextdp[j + A[i]] += 1
            else:
                P += 1
    dp = nextdp.copy()
print(P)
