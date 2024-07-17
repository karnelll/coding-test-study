mylist = []
for i in range(9) :
   mylist.append(int(input()))  			

print(max(mylist))						
print(mylist.index(max(mylist))+1)