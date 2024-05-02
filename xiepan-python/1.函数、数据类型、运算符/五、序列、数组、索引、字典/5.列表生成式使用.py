import random
lst = [item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

#通过random随机生成1到100的整数，for控制列表元素数量
lst2=[random.randint(1,101) for i in range(1,11)]
print(lst2)

#从列表中选择符合条件的元素，组成新的列表
lst3=[i for i in range(1,11) if i%2==0]
print(lst3)