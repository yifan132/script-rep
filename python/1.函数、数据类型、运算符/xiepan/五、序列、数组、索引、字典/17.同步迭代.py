fruits={'apple','pear','orange'} #字典类型，可变，若要不变，可改为列表[]
counts=[2,10,3]
f_c=zip(fruits,counts)
#print(dict(f_c))

for key,value in dict(f_c).items():
    print(key,'-->',value)
    print(key)
    match key:
        case key:
            print('有',value,'个',key)
       # case 'pear',