N,K = map(int,input().split())
a = list(map(int,input().split()))
b = [[] for i in range(K)]
for i in range(N):
  b[i%K].append(a[i])

for j in range(K):
  b[j].sort()


c = []
for i in range(N):
  c.append(b[i%K][i//K])
sorted_a = sorted(a)
if c == sorted_a:
  print('Yes')
else:
  print('No')
