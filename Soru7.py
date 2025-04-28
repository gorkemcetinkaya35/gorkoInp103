my_list = [1,3,7,"a",1]
new_list=[]
for i in range(len(my_list)):
    new_list.append("item["+str(i)+"]")
print(new_list)