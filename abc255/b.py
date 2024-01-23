N,K = map(int,input().split())
A = list(map(lambda x: int(x) - 1,input().split()))
XY = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    tmp = 10**12
    for j in range(K):
        dist = ((XY[i][0] - XY[A[j]][0])**2 + (XY[i][1] - XY[A[j]][1])**2)**0.5
        tmp = min(tmp, dist)
    ans = max(ans,tmp)
print(ans)