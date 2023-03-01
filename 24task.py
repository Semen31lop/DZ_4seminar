k=int(input(':'))
arr=list()
for i in range(k):
    p=int(input(" :"))
count=list()
for i in range(len(arr)-1):
    count.append(list[i-1]+list[i]+list[i+1])
count.append((list[-2]+list[-1]+list[0]))
print(max(count.append))
