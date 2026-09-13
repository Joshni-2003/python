

a="joshni"
def func():
  a="janu"
  print(a)
func()
print(a)




# global keyword:smae variable-to change the global variable value
a="joshni"
def func():
  global a
  a="janu"
  print(a)
func()
print(a)



# nonlocal keyword:nested function compulsory-to change the local variable value
def a():
  name="janu"
  def b():
    nonlocal name
    name="joshni"
    print(name)
  b()
  print(name)
a()


# keyword arguments:multiple keyword arguments.

def fun(**abc):
  print(abc)
#   print(abc["name"])
fun(name="janu",age=23)


def a(**a):
  for i in a:  
    print(i)       # i-means keys:name,age
a(name="joshni",age=23)

def a(**a):
  for i in a:
    print(a[i])      # a[i] menas values:joshni,23   a["name"].  i means keys.
a(name="joshni",age=23)




def a(**a):
  # print(a)
  for i in a:
    if type(a[i])==int:
      print(a[i])
  
a(name="joshni",age=23)



def a(**a):
  # print(a)
  for i in a.values():
    if type(i)==int:
      print(i)
  
a(name="joshni",age=23)


