N = int(input())

f = [i for i in range(1,N+1)]
for i in range(2,N+1):
    x = i**2
    if (x>N): break
    for j in range(x,N+1,x):
        while f[j]%x == 0:
            f[j] //= x
c = [0] * (N+1)
for i in range(N+1):
    c[f[i]] += 1
ans = 0
for i in range(N+1):
    ans += c[i]**2
print(ans)
    