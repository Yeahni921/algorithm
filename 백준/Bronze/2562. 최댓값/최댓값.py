data = [int(input()) for i in range(9)]

for i in range(9):
    if data[i] == max(data):
        print(data[i], i+1 , end = " ")