n1=(int(input(": ")))
list_1=[]
for i in range(n1):
    num = int(input(" : "))
    list_1.append(num)
print(list_1)


n2=(int(input(": ")))
list_2 = []
for i in range(n2):
    num = int(input(" : "))
    list_2.append(num)
print(list_2)


num_list3 = list_1+list_2

print(num_list3)
checked_nums_list = []
for i in num_list3:
    if num_list3.count(i) > 1 and i not in checked_nums_list:
       checked_nums_list.append(i)     
       print(i)