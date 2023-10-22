grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

numer = 0
denom = 0
for _ in range(20):
    class_name, score, score2 = input().split()
    if score2 == 'P':
        continue
    numer += (float(score) * grade[score2])
    denom += float(score)
print(numer/denom)