'''a=[1,2,3,4]
print(sum(a))
sum=0
for i in a:
    sum+=i
print(sum)



a=[12,24,45,56]
print(max(a))
largest=0
for i in a:
    if i>largest:
        largest=i
print(largest)


a=[1,2,3,4]
first=a[0]
for i in range(len(a)-1):
    a[i]=a[i+1]
a[len(a)-1]=first
print(a)

a=[1,2,3,4]
last=a[-1]
for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
a[0]=last
print(a)'''

def a(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end=end-1
arr=[1,2,3,4]
n=len(arr)
# a(arr,1,4)
a(arr,0,3)
print(arr)


