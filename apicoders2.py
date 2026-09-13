import requests
apiurl="https://jsonplaceholder.typicode.com/posts"

# apiurl1="https://dummyjson.com/products"
response=requests.get(apiurl)


if response.status_code==200:
    data=response.json()
    print(data,"data")
    for i in data:
        if i["id"]<=5:

            print(i["title"],"title")

    # data=response.text
    # print(data)
