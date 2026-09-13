# x=y=z="hello world"
# print(z)

# print("Hello","World")


# y='john'
# print(type(y))
# x=5
# print(type(x))

# a=frozenset([1,2,3,4])
# print(a)



# a="hello, world"
# print(a.replace(","," "))


# x=5
# y=3.14
# z="Hello"
# print(type(x))
# print(type(y))
# print(type(z))

# print(int(35.880))

# x=9
# print(f"The Price is {x:.2f} dollars")


# x="Welcome"
# print(x[3:5])

# a="Joshni"
# print(a.upper())

# txt="Hello,World!"
# print(txt)
# print(txt[2:5])
# txt.upper()
# print(txt)
# print(txt.upper())
# a="Python"
# print(f"I love {a}")


# a=[1,2,3,"hello"]
# print(a)
# print(type(a))
# print(a[3])
# a[0]=False
# print(a)

# b=(1,2,3,"python")
# print(type(b))
# print(b[2])



# x={1,2,3,4,3}
# print(type(x))
# x.update([5])
# # print(x)
# x.discard(10)
# print(x)
# x.pop()
# print(x)


# a={"name":"joshni","age":23,"role":"asseng"}
# print(a["name"])
# a["name"]="janu"
# print(a)
# a.update({"color":"white"})
# print(a)
# a.pop("color")
# print(a)
# a.popitem()
# print(a)


# z=[1,"hello",False]
# y=z.copy()
# print(y)

# import datetime
# x=datetime.datetime.now()
# print(x)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# import numpy as np
# res=np.prod(range(1,6))
# print(res)



# p=10000
# t=2
# r=5
# Amount=p*(1+r/100)**t
# compond_int=Amount-p
# print(Amount)
# print(compond_int)


# p=float(input("enetr:----"))
# t=float(input("enter:----"))
# r=float(input("enter:----"))
# a=p*pow((1+r/100),t)
# cp=a-p
# print("Amount is",a)
# print("compound interest is",cp)

# n=153
# digits=list(map(int,str(n)))
# cubes=list(map(lambda x:x**3,digits))
# total=sum(cubes)
# if total==n:
#     print("armstrong")
# else:
#     print("not")

# n=153
# temp=n
# def armstrong(n):
#     if n==0:
#         return 0
#     return(n % 10)** 3+armstrong(n // 10)

# res=armstrong(n)

# if res==temp:
#     print("armstrong")
# else:
#     print("not")



# n=int(input())
# if n>75:
#     print("distinction")
# else:
#     print("fail")


# a="Hello world"
# b=a.split()
# # print(b)
# c="".join(b)
# print(c)


# def concatenate():
#     a="hello"
#     b="world"
#     print(a+' '+b)
# concatenate()




# def fun(a , b):
#     return a + b
 
# a="hello"
# b="world"
# result=fun(a, b)
# print(result)



# def concat():
#     return a+b
# a="joshni"
# b="venu"
# print(concat())



# a=frozenset([10,20,30,20,20])
# # a.add(39)
# # a.remove(40)
# # print(a)

# # print(a)
# print(a[0])
# print(a)



# a={1,2,3,4,3,2}
# b=a.update({5,6})
# print(a)


# a=b"joshni"
# # print(type(a))
# a[0]=21
# print(a)


# a=bytearray([1,2,3,4,3])
# a[0]=50
# print(a[1])
# a.append(100)
# print(a)



# a=bytearray([1,2,3,2])
# a=b"hello"
# b=memoryview(a)
# print(b)

# a={"name":"joshni","age":23}
# # print(a)
# a["studname"]=a["name"]
# del a["name"]
# print(a)


# a="Hello World"
# print(a[6::])




# n=int(input("enter:-----"))
# a="distinction" if n>75 else "fail"
# print(a)



# a=input("enter :----")
# if a=="abc":
#     if 10==10:
#         if True:
#             print("vamsi")
# else:
#     if 100==100:
#         pass
#     else:
#         print("hyd")



for abc,xyz in {"name":"joshni","age":23}:
    print(abc,xyz)











