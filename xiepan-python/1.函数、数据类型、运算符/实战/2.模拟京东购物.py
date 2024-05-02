#创建一个空列表，用于存储商品入库信息
lst=[]
for i in range(5):
    goods=input('请输入库存商品信息，包含商品编码及名称，每次只能输入一件商品：')
    lst.append(goods)

#输出已入库商品
for item in lst:
    print(item)
    
#创建购物车列表
cart=[]
while True:
    flag=False #代表没有库存商品情况
    num=input('请输入要购买的商品编号：') 
    
    #遍历商品列表，查询要购买的商品是否存在
    for item in lst:
        if num==item[0:4]:
            flag=True
            cart.append(item)
            print(item,'商品已添加到购物车')
            break #退出for循环
    
    if not flag and num!='q': #not flag 为 flag=False
        print('商品不存在！')
        
    if num=='q':
        break #跳出while循环
    
print('-'*40)
print('购买的商品为：')
cart.reverse()
for i in cart:
    print(i)