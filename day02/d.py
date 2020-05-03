for j in range(0,5):
    for i in range(0,5-j):
        sp = ''*j
        print(sp,end='')
        print('*',end='')
    print()

    for i in range(6):
        print(i)

    l1=list(range(7,100,9))
    print(l1)

#本金10000，年利率千分之3，五年
rmb = 10000
for i in range(5):
    rmb *= 1.003
print('本金和%.2f' %rmb)
print(rmb)

i = 5
rmb = 10000
while i>0:
    rmb *= 1.003
    i -= 1
print('本金和%.2f' %rmb)
print(rmb)