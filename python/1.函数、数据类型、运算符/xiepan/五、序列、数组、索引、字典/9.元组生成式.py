t=(i for i in range(1,4))
print(t)
# t=tuple(t)
# print(t)

#遍历
# for i in t:
#     print(i)

#用__next__取出元组的元素，取出两个
print(t.__next__())
print(t.__next__())

#元素取出后，再将第一行的t转成元组，已经取出的元素就不存在了
t=tuple(t)
print(t)