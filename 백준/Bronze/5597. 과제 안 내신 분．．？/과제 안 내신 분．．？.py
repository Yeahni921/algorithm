all = [i for i in range(1,31)]

for _ in range(28):
    data = int(input())
    all.remove(data)
print(min(all))
print(max(all))