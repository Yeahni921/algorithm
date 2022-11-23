N = int(input())
score = list(map(int, input().split()))

new = []
for i in score:
    new.append(i/max(score)*100)

avg = sum(new)/N
print(avg)