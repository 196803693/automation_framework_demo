vec = [2, 4, 6]
vec2 = [3*x for x in vec]
print(vec2)

# str = input('请输入任意数据：')
# c_alpha,c_digit,c_space = 0,0,0
# for i in range(len(str)):
#     if str[i].isdigit():
#         c_digit += 1
#     elif str[i].isalpha():
#         c_alpha += 1
#     elif str[i].isspace():
#         c_space += 1
# print('英文/汉字有',c_alpha,'数字有',c_digit,'空格有',c_space)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
print(matrix)
conv_matrix = [[row[i] for row in matrix] for i in range(4)]
print('转换后',conv_matrix)

l2=[1,2e+8,2j+9,True,'hello','hello']
print(l2[:])
print('[1:]',l2[1:])
print('[:-1]',l2[:-1])
print('[::-2]',l2[::-2])
l3=['world' if x=='hello' else x for x in l2]
print('将hello替换成world',l3)

str1='sdgasagdaasa2351253   '
str2=str1.replace('a','A',4)
print(str2)

L = [i**2 for i in range(10)]
print(L)