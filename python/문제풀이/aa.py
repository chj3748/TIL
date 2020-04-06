def func(a,b=1,c=2,*args,**kwargs):
    d=sum([n*2 for n in args if n>2])
    e=sum([v**2 for v in kwargs.values()])
    return a+b+c+d+e

print(func(2,4,6,1,3,5,x=2,y=3))

# sd={}
# for i in enumerate(range(4)):
#     sd[i[0]]=i[1]

# print(sum(sd.values()))

# print('hi')
# if True
#     print('hello')

# def my_sum(a,b):
#     print('sdf')
# result=my_sum(1,2)
# print(result)

# a=1
# def f1():
#     a=5
#     f2()
# def f2():
#     print(a,end='')
# f1()
# print(a)

# print(-3 **2+3)
# name=1
# print('hello {%name%}')

# import random

# random.sam

# print(3 and 5)
# print(bool(5))

# try:
#     num='absc'
#     100/int(num)
# except Exception:
#     print(111)
# except ValueError:
#     print(222)
# finally:
#     print(333)

# greeting='hello'
# print(hello)

# def f(c,b,a):
#     return a*b+c

# print(f(2,5,4))

# result=4+True+False+5
# print(result)

# class Espresso:
#     def recipe(self,shot):
#         print(f'espresso {shot}shot')

# class Latte(Espresso):
#     def recipe(self,shot,milk):
#         print(f'espresso {shot}shot ,  milk {milk}')

# l=Latte()
# l.recipe()

# names='james'
# print(names[-2])

# class Person:
#     population=0
#     def __init__(self,name):
#         self.name=name
#         Person.population+=1

# p1=Person('sdf')
# p2=Person('sdf')
# p3=Person('sdf')

# print(Person.population)

# import copy
# list1=[3,'a','b']
# list2 = [1,2,list1]
# l3=list1[:]
# l4=copy.copy(list2)
# l5=copy.deepcopy(list2)
# l5[2][1]=3
# print(l5[2][1])

# class dog:
#     def __init__(self, name='강'):
#         self.name=name

#     def bark(self):
#         print(f'{self.name}:멍멍')
# d1=dog('바둑이')
# d2=dog()
# d1.bark()
# print(d1.name)
# print(d2.name)
# d2.bark()

# word='python'
# indexing=word[3:8]
# print(indexing)

# f={'a':'사','b':'바'}
# a=f.get('a')
# b=f.get('cherry')
# c=f.get('melon',True)
# d={a:b}
# if c:
#     print(d)

# numbers=range(1,10,3)
# print(len(numbers))

# def mf(n):
#     return n**3

# def mf2(n):
#     return n%2

# numbers=[1,2,3]
# nn=list(filter(mf2,(map(mf,numbers))))
# print(nn)
# c=['k','c','g']
# c.extend('sdf')
# print(c)

# num=10
# def plus():
#     print(num)
#     num+=1
# plus()
# print(num)
# class Myclass:
#     @classmethod
#     def class_method(cls):
#         return cls
#     @staticmethod
#     def static_method(arg):
#         return arg
# mc=Myclass()

# print(mc.class_method())
# print(mc.static_method())
