a='python'
print(a[::-1])


b='hello world'
rev=''
for i in b:
    rev=i+rev
print(rev)


n=int(input('enetr:'))
a=0
b=1
for i in range(1,n+1):
    print(a)
    c=a+b
    a=b
    b=c



n=int(input('enter:'))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(i):
        print('*  ',end=' ')
    print()
        


a=int(input('enter:'))
for i in range(1,a+1):
    for j in range(i):
        print('*',end='')
    print()

x=int(input('enter:'))
for i in range(1,x+1):
    print('*',end='')
    for j in range(i-1):
        print('*',end='')
    print()



z=int(input("enter:"))
for i in range(z,0,-1):
    for j in range(i):
        print('*',end='')
    print()







