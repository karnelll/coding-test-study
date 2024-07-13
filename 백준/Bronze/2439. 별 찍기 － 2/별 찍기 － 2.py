import sys

T = int(sys.stdin.readline().strip())

for i in range(1, T + 1):
    print(' ' * (T - i) + '*' * i)
