a = [list(map(int, input().split())) for _ in range(9)]
    
max_num = 0
max_row = 0
max_col = 0

for row in range(9):
    for col in range(9):
        if a[row][col] >= max_num:
            max_row = row+1
            max_col = col+1
            max_num = a[row][col]
            
print(max_num)
print(max_row, max_col)