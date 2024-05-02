s=0
i=1

for i in range(1,101):
    if i%2==1:
        continue
    s+=i
print('和是：',s)

year=eval(input('年份：'))
if (year%4==0 and year%100!=0) or year%400==0 :
    print(year,'是闰年')
else :
    print(year,'是平年')