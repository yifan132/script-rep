data=eval(input('请输入：'))

match data:
    case {'xx':'a','zz':'b'}:
        print('字典')
    case [10,20,30]:
        print('列表')
    case (1,2,3):
        print('元组')
    case _:
        print('没有匹配以上任何条件，相当于多重IF中的else')