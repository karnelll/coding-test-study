X = int(input())
N = int(input())

total_check = []

for N in range(N):
    A, B = map(int, input().split())
    total_check.append(A*B)

total_sum = sum(total_check)

if X == total_sum:
    print('Yes')
else:
    print('No')