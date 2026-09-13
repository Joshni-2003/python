print("python calling with fakestoreapi")

import requests
apiurl="https://fakestoreapi.com/products"

print(requests.get(apiurl))


response=requests.get(apiurl)

if response.status_code==200:
    # a=response.text   #text means str
    a=response.json()   # dict
    print(a)
    print(type(a))      #list
    for i in range(len(a)):
        # print(a[i],"item in lst")
        if a[i]["category"]=="men's clothing":
            print(a[i]["title"],"mens clothing")
    
else:
    print("response is not matching")
