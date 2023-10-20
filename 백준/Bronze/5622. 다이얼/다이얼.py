word = input()

dic = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}

count = 0
for i in word:
    for j in dic:
        if i in j:
            count += dic[j]
print(count)