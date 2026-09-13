# module:python contain python code(functions,classes,variables) that can be imported and used 
# built in modules:math,datetime and OS 
# external modules:numpy,pandas,requests
# math:sqrt,floor,ceil,abs


import math
num=math.sqrt(25)
print(num)  #5.0
print(int(num))

import math
num=math.sqrt(567)
b=math.floor(num)
print(b)

import math
a=math.pow(5,2)  #base values,power value
print(a)

import math
print(math.ceil(2.5))

import math
x=-10
print(math.fabs(x))


json : string
import json
a=[{"name":"joshni","age":23},{"name":"venu","age":24}]
print(type(a))
b=json.dumps(a)
print(b)
print(type(b))
print(b[1]["age"])  # it gives error because it is string 0-[,1-{,n-2,a-3 like that 



import json
a='[{"name":"ram"},{"name":"rani"}]'
print(type(a))
b=json.loads(a)
print(b)
print(type(b))
print(b[0]["name"])  # list b[0]-first dict,b[1]-second dict



datetime module (bulitin module)
import datetime
print(datetime)
print(type(datetime))

import datetime
a=datetime.date.today()  #it gives only date of the day 
print(a)

import datetime
b=datetime.datetime.now()  # it gives both date and time
print(b)

import datetime
b=datetime.datetime.now().time()  # it gives only time
print(b)

c=b.hour
print(c,"hr")

d=b.minute
print(d,"min")

v=b.second
print(v,"sec")


import datetime
x=datetime.datetime.now()
print(x)

y=x.date()
print(y)

d=y.year
print(d)

u=y.month
print(u)

z=y.day
print(z)


import datetime
a=datetime.datetime.now().date()
print(a.weekday())
print(a.strftime("%A"))



import datetime
a=datetime.datetime.now().date()
# print(a)
print(a.weekday)
b=a+datetime.timedelta(days=10)
print(b)



import datetime
past=datetime.date(2003,3,27)
present=datetime.date(2026,8,21)
diff=present-past
print(diff)