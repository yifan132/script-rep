lst=[88,89,90,98,00,99]
print(lst)

#方法一
# for value in range(len(lst)):
#     if lst[value] ==0 :
#         print(lst[value])
#         print(len(lst))
#         lst[value]='200'+str(lst[value])
#     else :
#         lst[value]='19'+str(lst[value])
# print(lst)

#方法二
for index,item in enumerate(lst):
    print(index,item)
    if item == 0:
        lst[index]='200'+str(item)
    else:
        lst[index]='19'+str(item)
print(lst)