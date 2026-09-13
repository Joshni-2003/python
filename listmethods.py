a=[5,2,True,[6,7]]
print(a)
print(type(a))
a.append(False)  # add the element at the end of the list
print(a)
print(a)
a.insert(2,{"name":"joshni","age":23}) # add the elment at particular index position
print(a)
a.remove(5)
# a.pop(0)   # to remove the element at specified index
print(a)
b=[1,2,3,4,8,9]
a.extend(b)
print(a)
a.clear()   # clear all elements in list
print(a)


x=["apple","mango","banana","orange"]
del x[0:2]
del x[0:1]
print(x)

del x[0:3]
print(x)



a=["pk","mb","ntr","rc","aa"]
b=a[0:5:2]
print(b)
print(a[::-1])

a=[i**2 for i in range(10)]
print(a)

squares=[i  for i in range(1,5) if i%2==0 ]
print(squares)

squares=[i  for i in range(0,5,2) ]
print(squares)



a=[[1,2,3],[3,4],[5,6,7]]
b=[]
for i in a:
    for j in i:
        if j not in b:
            b.append(j)
print(b)



a=[10,20,["vamsi",True],["vamsi2",["1","2"]],"True"]
b=[]
for i in range(len(a)):
    for j in (i):
        b.append(j)
print(int(b))

for i in range(10):
    if i%2==0:
        print(i)

for i in range(0,10,2):
    print(i)

a=[i for i in range(0,10,2)]
print(a)


a=["sdfgh","asfg","qwer"]
a.reverse()  # to reverse the list
print(a)


a="vamsi"
print(a[::-1])
a.split()
print(b)
a.reverse()
print(a)
c="".join(b)
print(c)

# to flatten the list , interview qn

a = [10, 20, ["vamsi", True], ["vamsi2", ["1", "2"]], "True"]
# print(len(a))
b=[]
for i in a:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for k in j:
                    b.append(k)
            else:
                b.append(j)
    else:
        b.append(i)
print(b)
    

a="vamsi"
b=list(a)
b.reverse()
# print(b)
c="".join(b)
print(c)


a="joshni venu"
b=a.split()
b.reverse()
c="".join(b)
print(c)

a=[1,2,3,2,2,3,3,3]
print(a.count(3))
c=a.count(3)
print(c)


a=[1,2,3,4,3,2,1]
a.sort()  # sort list in ao
a.sort(reverse=True)
print(a)

b=[1,2,3,4,2]
print(b.index(4))

a=["pk","mm","aa","nani"]
for i,j in enumerate(a):
    print(i,j)


a={"name":"josni","age":23}
for i,j in a.items():
    print(i,j)

for i in a.values():
    print(i)

for i in a.values():
    print(i)


a["studentname"]=a["name"]
del a["name"]
print(a)
