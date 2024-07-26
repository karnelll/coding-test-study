numbers = input().split() 
reserve_number = [number[::-1] for number in numbers]
print(max(reserve_number))  