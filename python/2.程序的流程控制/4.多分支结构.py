score=eval(input('输入成绩：'))

#多分支结构
if score < 0 or score>100:
    print('你输入的成绩',score,'成绩有误')
elif 0<= score < 60:
    print('你输入的成绩',score,'评分C') 
elif 0<= score < 80:
    print('你输入的成绩',score,'评分B') 
elif 0<= score < 90:
    print('你输入的成绩',score,'评分A') 
else:
    print('你输入的成绩',score,'评分A+') 