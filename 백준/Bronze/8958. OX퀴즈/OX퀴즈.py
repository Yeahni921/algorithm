n = int(input())

for i in range(n):
    data = list(input())
    score = 0
    sum_score = 0
    for ox in data:
        if ox =='O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
    