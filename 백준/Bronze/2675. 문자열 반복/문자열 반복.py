t = int(input())

for _ in range(t):
    r, s = input().split()
    text = ''
    for i in s:
        text = text + i*int(r)
    print(text)