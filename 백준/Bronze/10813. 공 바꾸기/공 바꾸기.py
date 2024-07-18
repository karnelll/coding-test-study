N, M = map(int, input().split())
basket = [i for i in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    basket[x], basket[y] = basket[y], basket[x]

for i in range(1, N + 1):
    print(basket[i], end=' ')
