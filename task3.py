a=[1,'apple',True,'apple']
print(a)
print(type(a))
print(a[0])
print(len(a))
print(a[2])
b=list((1,3))
print(type(b))
a[3]='banana'
print(a)
a.append('pink')
print(a)
a.insert(0,'0')
print(a)
b=['bat','ball']
a.extend(b)
print(a)
a.remove("apple")
print(a)
a.pop(0)
a.pop()
print(a)
#a.clear()
print(a)
for i in a:
    print(i)


for i in z:
    print(i)
for i in range(len(z)):
    print(z[i])
i=0
while i<len(z):
    print(z[i])
    i=i+1

#[print(i) for i in z]




z=['cow','carrot','rabbit','cow']
a=[]
for i in z:
    if 'c' in i:
        a.append(i)
print(a)


b=['cow','bat','rat','zebra']
b.sort(reverse=True)
print(b)

b.reverse()
print(b)




u=[12,2,3]
v=u.copy()
print(v)

q=[1,2,3]
w=[4,5,6]
e=q+w
print(e)

from array import array
arr=array('i',[1,2,3,4])
for i in arr:
    print(i)

a=array('i',[1,2,3])
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)
