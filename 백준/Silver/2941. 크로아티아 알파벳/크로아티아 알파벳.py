word = input()

alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in alp:
    word = word.replace(i, '*')
print(len(word))