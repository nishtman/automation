import requests
#this comment added by remote
# this line to check version control added in remote

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
if response.status_code == 200 :
    data = response.json()
    print("data received")
    print(data)
else :

    print("error in receiving data" , response.status_code)

    print("error in receiving data" , response.status_code)

    print("error in receiving data" , response.status_code)


    # added by local automation

