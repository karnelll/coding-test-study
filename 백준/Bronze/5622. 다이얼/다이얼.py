alpabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
time = 0

for x in S:
    for unit in alpabet_list:
        if x in unit:
            time += alpabet_list.index(unit) + 3
            break

print(time)