N, M = map(int, input().split())
basket = [i + 1 for i in range(N)]  

for _ in range(M):
    x, y = map(int, input().split())
    basket[x-1:y] = basket[x-1:y][::-1] 

print(*basket)