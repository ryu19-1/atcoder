def validate(value):
    return A + D * value < X


X, A, D, N = map(int, input().split())
if D < 0:
    D = -D
    X = -X
    A = -A
if X <= A:
    print(A - X)
elif A + D * (N - 1) <= X:
    print(X - A - D * (N - 1))
else:
    # A+D*k < Xを満たす最大のkを見つける
    left = -1
    right = N
    k = 0
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if validate(mid):
            k = mid
            # print(k, validate(mid))
            left = mid
        else:
            right = mid
    print(min(abs(X - (A + D * k)), abs(X - (A + D * k + D))))
