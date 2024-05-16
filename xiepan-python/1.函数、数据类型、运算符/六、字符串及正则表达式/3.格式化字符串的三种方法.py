#(1)用占位符进行格式化
name='小李'
age=18
score=98.5

#%s是字符串格式，%d是十进制整数格式，%f是浮点数格式，在后面跟一个元组显示
print('姓名：%s,年龄：%d,成绩：%f' % (name,age,score))

#调整浮点的显示小数位数
print('姓名：%s,年龄：%d,成绩：%.1f' % (name,age,score))

#(2)f-string，用{}占位
print(f'姓名：{name},年龄：{age},成绩：{score}')

#使用字符串format方法,{0},{1},{2}分别对应format中的3个参数索引
print('姓名：{0}，年龄：{1}，成绩：{2}'.format(name,age,score))
print('姓名：{1}，年龄：{2}，成绩：{0}'.format(score,name,age))