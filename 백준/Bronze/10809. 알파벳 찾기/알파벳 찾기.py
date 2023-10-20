s = input()

for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in s:
        print(s.find(i), end = ' ')
    else:
        print(-1, end = ' ')