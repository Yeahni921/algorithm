word = input()
word = word.upper()

word_cnt = list(set(word))

cnt = []
for i in word_cnt:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_cnt[cnt.index(max(cnt))])