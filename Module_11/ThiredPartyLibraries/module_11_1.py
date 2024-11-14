import requests


payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('https://httpbin.org/post', data=payload)

print(r.text)
print(r.status_code)
print(r.elapsed)

r = requests.get('https://google.com')
print(r.headers)

r = requests.put('https://google.com')
print(r.status_code)
