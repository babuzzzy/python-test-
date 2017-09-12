import requests

url = 'http//httpin.org/get'
headers = {'user-agent':'my-app/0.0.1'}
r = requests.get(url,headers=headers)
