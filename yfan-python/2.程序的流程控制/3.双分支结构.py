number=eval(input('输入中奖号码：'))

if number==123414:
    print('中奖了')
else:
    print('没中奖')
    
print('以上代码可以通过条件表达式进行简化')
#1
result='恭喜你中奖了' if number==123 else '没中奖'
print(result)

#2
print('恭喜你中奖了' if number==123 else '没中奖')