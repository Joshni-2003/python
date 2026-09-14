# api call:--get:---store
# 20 dict or 100 dict

#only one blueprint
#20 objects


# fakestore api

# in order to make api calls with python we dont have any inbuilt module .so we need third party library which is requests
# to install third party library we use the command :------- pip install requests
# after installation we have to import it./



# there are main differences:--------


a={"name":"joshni","age":23,"role":"eng"}
for i in a:
    # print(i)
    print(a[i])


a=[{"name":"joshni","age":23},{"name":"janu","id":101}]
for i in a:
  print(i["name"])










import requests
apiurl="https://fakestoreapi.com/products"
response=requests.get(apiurl)
# print(response)     # <Response [200]>   ----->response was done successfull..
if response.status_code==200:
    data=response.json()
    # print(type(data))    # <class 'list'> ---->so we can iterate the list...
    # print(data)
    for i in data:  # i--variable
        # print(i)
        # print(len(i))
        print(i["title"])






import requests
apiurl="https://fakestoreapi.com/products"
response=requests.get(apiurl)
# print(response)     # <Response [200]>   ----->response was done successfull..
if response.status_code==200:
    data=response.json()
    
    class fakestoreapiproduct:
        def __init__(self,t,p,c):
            self.title=t
            self.price=p
            self.category=c
            print(f"{self.title} with the price {self.price} with {self.category}")
          
    for i in data:  # i--dict
               
        title=i["title"]
        price=i["price"]
        category=i["category"]

        
        
        fakestoreapiproduct(title,price,category)



