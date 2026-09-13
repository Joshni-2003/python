import requests
apiurl="https://dummyjson.com/products"
response=requests.get(apiurl)
if response.status_code==200:
    data=response.json()
    print(type(data))
    for i in data["products"]:
        if i["price"] == 9.99:
            print(i["price"], "data")

    
    #       print(i["price"],i["title"],"data")

    