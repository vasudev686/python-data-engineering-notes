import requests

# response = requests.get("https://dummyjson.com/products")
# print(response.status_code)
# print(response.json())


#status_code:
#200 - OK
#404 - Not Found

#Understanding the API Endpoints

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())
