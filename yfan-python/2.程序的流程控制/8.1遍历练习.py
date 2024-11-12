#计算1-100之间的偶数和#
sum=0
a=1
while a<= 100:
    if a%2==0: #算奇数也可以这样写 if a%2:
        sum+=a
    a+=1
print(sum)

#计算100-999之间的水仙花数
#例如：153=1^3+5^3+3^3
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    #print(bai,shi,ge)
    
    #判断
    if ge**3+shi**3+bai**3==item:
        print(item,'是水仙花数')
        
    
    
#break控制语句
for i in range(5): #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            break
        print(j)
        
        
#continue控制语句
for i in range(5): #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')