n, m = map(int, input().split())   # n개 바구니, m: 바귀니의 순서 바꿀 횟수

basket = [x for x in range(1, n+1)]    
for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        basket[i-1:j] = basket[j-1::-1]
    else:
        basket[i-1:j] = basket[j-1:i-2:-1]

for i in range(n):
    print(basket[i], end = ' ')