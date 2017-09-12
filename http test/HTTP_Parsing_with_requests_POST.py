import requests

r = requests.post('http://httpin.org/post', data = {'key':'value'})

print(r.text)
print(r.status_code)

