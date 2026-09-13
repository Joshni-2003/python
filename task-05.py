# List
# a=(1,2,3)
# print(a)
# print(type(a))
# a=(1)
# b=(1,)
# print(type(a))
# print(type(b))
# tuple=(1,False,'cat',5)
# print(tuple[0])
# print(len(tuple))

# a=(1,2,3,4,5)
# print(a[-1])
# print(a[:3])
# print(a[1:])
# print(a[1:4])
# print(a[-4:-2])


# b=(1,2,False,'sdfg','fghjk')
# if "sdfg" in b:
#     print("true")




# x=(1,2,3,4,5)
# y=list(x)
# y.append('10')
# z=tuple(y)
# print(z)


# x=(1,2,3)
# y=(4,)
# x=x+y
# print(x)


# a=(1,2,3,4,5,'bat')
# b=list(a)
# b.remove('bat')
# c=tuple(b)
# print(c)

# a=(1,2,3)
# for i in a:
#     print(i)


# a=(1,2,3,4)
# for i in range(len(a)):
#     print(a[i])

# a=(1,2,3,4,5)
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1

# x=(1,2)
# y=(3,4)
# z=x+y
# print(z)


# x=(1,2,3,4,5,22,2,2)
# print(x.count(2))
# print(x.index(22))


# Set
# a={1,True,"hello","python"}
# print(type(a))
# print(a)
# print(len(a))

# for i in a:
#     print(i)

# if "python" not in a:
#     print("true")
# else:
#     print("false")
# a={1,2,3}
# a.add("program")
# print(a)

# a={"bat","cat"}
# # b={"dog","fish"}
# b=("dog","fish")
# a.update(b)
# print(a)

# x={"hii","python","programming"}
# x.remove("hello")
# print(x)
# x.discard("hello")
# print(x)
# x.pop()
# print(x)
# x.clear()
# print(x)

# for i in x:
#     print(i)


# a={1,2,3}
# b={3,5,6}
# c=a.union(b)
# print(c)
# a.update(b)
# print(a)
# c=a.intersection(b)
# print(c)
# c=a.difference(b)
# print(c)
# c=a.symmetric_difference(b)
# print(c)


# Dictionaries
# a={"name":"janu","age":11,"city":"tiruvuru","name":"ammmu"}
# print(a)
# print(type(a))
# print(a["city"])
# print(a.get("age"))
# print(a.keys())
# print(a.values())
# print(len(a))
# a["name"]="venu"
# print(a)
# a.update({"name":"venu","age":23,"color":"blue"})
# print(a)
# a.pop("age")
# print(a)
# a.popitem()
# print(a)
# for i in a.values():

#     print(i)
# # print(a[i])

# for i in a.items():
#     print(i)

# a={"name":"janu","age":23}
# b=a.copy()
# b["name"]="joshni"
# print(b)
    
# # connditional stmnts

# a=5
# b=10
# if b>a:
#     print("true")


# a=-10
# if a>0:
#     print("positive")


# marks=92
# if marks<95:
#     print("distinct")
# elif marks<80:
#     print("A")
# elif marks<70:
#     print("B")
# else:
#     print("fail")

# age=19
# if age>=18:
#     print("yes")
# else:
#     print("no")

# n=3
# if n%2==0:
#     print("even")
# else:
#     print("odd")


# day=12
# match day:
#     case 1:
#         print("mon")
#     case 2:
#         print("tues")
#     case 3:
#         print("wed")
#     case 4:
#         print("thurs")
#     case 5:
#         print("fri")
#     case _:
#         print("nothing")


# n=8
# i=0
# while i<n:
#     print(i)
#     i+=1


# n=10
# i=0
# while i<n:
#     if i==5:
#         break
#     i=i+1
#     print(i)

# n=7
# i=0
# while i<n:
#     if i==5:
#         i=i+1
#         print(i)
#         continue
#     i=i+1

# i=0
# n=7
# while i<n:
#     i=i+1
#     if i==5:
#         continue
#     print(i)

# a=[1,2,3,4]
# for i in range (len(a)):
#     print(a[i])


# a=[1,2,"apple","banana"]
# for i in a:
#     if i=="banana":
#         break
#     print(i)
   
    # print(i)
    # if i=="apple":
    #     break

# a=['cat','bat','rat','mat']
# for i in a:
#     if i=='rat':
#         continue
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(2,12,5):
#     print(i)

# a=[1,2,3,4]
# for i in a:
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")


# for i in range(5):
#     print(i)
# else:
#     print("bye")


# for i in range(6):
#    if i==3:
#     break
#    print(i)
# else:
#     print("hi")


# In the loop, when the item value is "banana", jump directly to the next item.
# a=["apple","banana","orange","kiwi"]
# for i in a:
#    if i=="banana":
#       continue
#    print(i)
   

# Exit the loop when x is "banana".

# a=["apple","banana","orange","kiwi"]
# for i in a:
#     if i=="banana":
#         break
#     print(i)

# functions

# def a():
#     print("hello")
# a()
# a()
# a()


# def my_fun(x,y):
#     return x+y
# z=my_fun(10,20)
# print(z)


# def a():
#     return "hello world"
# b=a()
# print(b)

# def a(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(a(1,2,3))


# a=[1,2,3]
# large=0
# for i in a:
#     if i>large:
#         large=i
# print(large)

# def a(*args):
#     large=0
#     for i in args:
#         if i>large:
#             large=i
#     print(large)
# a(1,50,7,10)


# def a(a,b,c=10):
#     # print(a+b+c)
#     return a+b+c
# print(a(1,2))

# def a(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# a(1,2,3,4)


# def a(**kargs):
#     print(kargs)
# a(name="joshni",age=23)

# b=10
# def a():
#     a=20
#     # print(a+b)
#     c=a+b
#     print(c)
# a()


# a=10
# b=20
# def x():
#     return a*b
# print(x())
# print(a)


# def a():
#     x=100
#     print(x)
# a()



# x=100
# def a():
#     global x
#     x=200
#     print(x)
# a()

# def a():
#     global x
#     x=100
# a()
# print(x)




# def decorator(fun):
#     def inner():
#         print("welcome to python programming")
#         fun()
#     return inner
# # decorator(a)

# @decorator

# def a():
#     print("hello python")
# a()

# x=lambda a:a+10
# print(x(10))

# nums=[1,2,3,4]
# a=list(map(lambda x:x+2,nums))
# print(a)

# a=list(filter(lambda x:x%2==0,nums))
# print(a)

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# def a(n):
#     if n<=1:
#         return n
#     else:
#         return a(n-1)+a(n-2)
# print(a(5))

# def a():
#     # return 1
#     # return 2
#     yield 1
#     yield 2
#     yield 3
# # print(a())
# x=a()
# print(next(x))
# print(next(x))
# print(next(x))


# def a():
#     return 1
#     return 2
#     return 3
# # x=a()
# # print(x)
# print(a())
# print(next(x))
# print(next(x))

# def a():
#     yield 1
#     yield 2
#     yield 3
# for i in a():
#     print(i)

# def a():
#     for i in range(6):
#         yield i
# for i in a():
#     print(i)


# def a(n):
#     for i in range(n):
#         yield i*i
# for i in a(5):
#     print(i)

# def a():
#     sum=0
#     for i in range(5):
#         sum+=i
#         yield sum
# for i in a():
#     print(i)

# a=[x for x in range(5)]
# print(a)


# a=(x for x in range(5))
# # print(next(a))
# print(list(a))


# a=(sum sum+=i for i range(5) sum=0)
# print(a)

# a=sum( i*i for i in range(5))
# print(a)

# for i in range(10):
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(1,5,2):
#     print(i)

# a=["cat","rat","mat"]
# print(a[0])

# b=a[0]
# print(b)
# a[0]="bat"
# print(a)
# print(len(a))
# for i in a:
#     print(i)
# a.append("cot")
# print(a)
# a.pop(0)
# print(a)
# a.remove("mat")
# print(a)

# a=[1,2,3,4]
# it=iter(a)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# import module
# # module.a()
# x=module.list[0]
# print(x)


import datetime
x=datetime.datetime.now()
print(x)
print(x.year)

import datetime
x=datetime.datetime(2003,3,27)
print(x.strftime("%B"))


a=[1,2,3,4]
print(max(a))
print(min(a))
x=-2.3
print(abs(x))

# import math
x=pow(2,3)
print(x)
print(pow(2,3))
# x=math.sqrt(81)
# print(x)

# print(math.ceil(2.8))
# print(math.floor(2.2))
# print(max(5,10))





