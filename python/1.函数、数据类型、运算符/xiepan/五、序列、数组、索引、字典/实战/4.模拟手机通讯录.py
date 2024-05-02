#创建空集合用于存储姓名电话
s=set()
for i in range(1,6):
    info=input('请输入第'+str(i)+'位好友姓名及手机号：')
    s.add(info)
    
for item in s:
    print(item)