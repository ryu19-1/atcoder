N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

cumsumA = [0] * (N + 1)
for i in range(N):
    cumsumA[i + 1] = cumsumA[i] + A[i]

for j in range(Q):
    X = int(input())
    left = 0  # 0-indexed
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] < X:
            # ans = mid
            left = mid + 1
        else:
            right = mid - 1
    ans = left * X - cumsumA[left] + (cumsumA[N] - cumsumA[left]) - X * (N - left)
    print(ans)
