list1 = [3,5,-4,-1,0,-2,-6]
res = sorted(list1,key=lambda x:abs(x))
print(res)

sum = 0
for i in range(0,101):
    sum+=i
print(sum)

sum = 0
i = 1
while i <= 100:
    sum += i
    i+=1
print(sum)


i = 39
sum = 0
while i<=149:
    sum += i
    i+=1
print('累加之和',sum)

sum = 0
for i in range(1,101):
    if i%2==0:
        sum += i
        print(i,end=' ')
    else:
        continue
print('\n和是',sum)

#25-249,被7整除
sum=0
for i in range(25,250):
    if i%7 == 0:
        sum+=i
        print(i,end='')
print('\n和是',sum)