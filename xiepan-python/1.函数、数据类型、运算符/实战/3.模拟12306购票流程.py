#创建字典存储车次信息
dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8967':['北京南-天津西','18:20','19:19','00:59'],
    'G203':['北京南-天津南','18:35','19:09','00:34']
}
print('车次     出发站-到达站       出发时间        到达时间        历时时长')
#遍历
for key in dict_ticket.keys():
    print(key,end='\t')
    for item in dict_ticket.get(key): #根据键，获取值
        print(item,end='\t\t')
    #换行
    print()    
    
#输入用户购票车次
train_no=input('请输入要购买的车次：')
#获取购票车次信息
info=dict_ticket.get(train_no,'车次不存在！')

if info!='车次不存在！':
    usr_nm=input('请输入乘车人，若有多位乘车人，用逗号分隔：')
    print('您已购买了',train_no,'车次',',该车次出发时间为：',info[1])
else:
    print('对不起，选择的车次可能不存在！')