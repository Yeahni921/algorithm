n, m = map(int, input().split())
result = [0] * n
for a in range(m):
    i, j, k = map(int, input().split())
    result[i-1: j] = [k]*(j-i+1)

for _ in range(len(result)):
    print(result[_], end = ' ')