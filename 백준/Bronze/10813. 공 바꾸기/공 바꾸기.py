n, m = map(int, input().split())

result = []
for num in range(1, n + 1):
    result.append(num)

for _ in range(m):
    i, j = map(int, input().split())
    result[i-1], result[j-1] = result[j-1], result[i-1]
    
for k in range(len(result)):
    print(result[k], end = ' ')