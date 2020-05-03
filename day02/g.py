#100,50;50,25;25,12.5;
l1=[]
ori_hei = 100
l1.append(ori_hei)
for i in range(1,11):
    l1.append(ori_hei/2**i)
    l1.append(ori_hei/2**i)
print(l1)
print('总共经过的距离',sum(l1))
print(len(l1))
print('第十次反弹高度',l1[10*2])