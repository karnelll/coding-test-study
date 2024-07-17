N, X = map(int, input().split())
A = list(map(int, input().split()))

for value in A:
    if value < X:
        print(value, end=' ')