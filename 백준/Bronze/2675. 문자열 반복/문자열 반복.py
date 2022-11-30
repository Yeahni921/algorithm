t = int(input())

for i in range(t):
    num, x = input().split()
    text = ''
    for j in x:
        text = text + j*int(num)
    print(text)