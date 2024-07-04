A = int(input())
B = input()
ADD_list = [A * int(digit) for digit in B]
print(ADD_list[2])
print(ADD_list[1])
print(ADD_list[0])
final_result = ADD_list[2] + ADD_list[1]*10 + ADD_list[0]*100
print(final_result)