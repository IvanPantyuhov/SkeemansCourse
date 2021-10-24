import requests

response = requests.get('https://httpbin.org/ip').json()
print(f' IP is {response["origin"]}')