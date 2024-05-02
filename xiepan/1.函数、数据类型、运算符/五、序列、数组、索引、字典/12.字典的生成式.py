import random
d={item:random.randint(1,100) for item in range(4)}
print(d)

lst=[100,101,102]
lst2=['zhang','wang','xie']
d1={key:value for key,value in zip(lst,lst2)}
print(d1)