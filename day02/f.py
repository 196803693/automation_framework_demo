l1=['郭碧婷','屎','屎','尿','屁','肝脏','血管','筋骨','屎','屎','肠子','心脏','屎','卫生巾']
# l1.remove('屎')
# l1.pop(0)

#通过列表内容来删,简单
delname = '屎'
num = l1.count(delname)
# print(l1.index('屎'))
# num = 0
# for i in range(num):
#     l1.remove(delname)
# else:
#     print('没有要删的东西')
# print('删除后',l1)

#通过下标删除
# for i in range(num):
#     j=0
#     while j < len(l1):
#         if l1[j] == delname:
#             l1.pop(j)
#         j+=1
# print(l1)

l1=[x for x in l1 if x != delname]
print(l1)