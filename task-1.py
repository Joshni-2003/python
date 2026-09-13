a=10
print(a)
b="ghjk"
print(b)
# this is a single line comment
'''
multi
line
comments
'''
a=1,2,3
print(a)
a,b=1,2
print(a)
print(b)

a=b=c=1
print(a)

a=[1,2,3]
x,y,z=a
print(x)
print(z)

a='hello'
def fun():
    b='programming'
    print(f"{a} python {b}")
fun()


'''a="hi"
def funct():
    global a
    b="heyy"
    print(f"{a} good morning")
funct()

a="awesome"
def x():
    print(a)
x()'''

a="awesome"
def x():
    global a
    a="fantastic"
    print(a)
x()
print(a)

a=5
print(type(a))
b=3.14
print(type(b))
c=3+5j
print(type(c))
x='string'
print(type(x))
y=[1,2,3]
print(type(y))
z=1,
print(type(z))

v={'name':'joshni','age':23}
print(type(v))

a={1,2,3,2}
print(type(a))

d=frozenset([1,2,3])
print(d)

a=5
b=float(a)
print(b)

'''a='joshni'
b=int(a)
print(b)'''

a="Welcome to python programming language"
print(a)
print(type(a))
print(len(a))
print(a.count('e'))
print(a.upper())
print(a.strip())
print(a.endswith('language'))
print(a.startswith('welcome'))

x='i am doing task now'
print(x[::-1])

z='programming'
print(z[:4])
print(z[-5:])
print(z[1:])
print(z[:-1])
print(z[3:8])
print(z[::3])
print(z[::-2])

m='welcome to progminglang'
#print(a.split())


a='joshni'
b='girl'
print(a+'is'+b)

print(m.capitalize())
print(m.title())
print(m.index[1])



# name="joshni"
# age=23
# print(f"my name is {name} and age is {age}")


try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("cant divide by zero")
else:
    print("hello")
finally:
    print("bye")