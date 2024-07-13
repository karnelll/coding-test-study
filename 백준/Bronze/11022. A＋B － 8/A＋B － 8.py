import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    C = A + B
    print(f'Case #{i}: {A} + {B} = {C}')