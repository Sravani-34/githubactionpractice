import requests

res=requests.get("http://www.google.com")
print(res)
print(res.text)
print(res.status_code)
print(res.cookies)
print(res.url)
