
import requests

msg = 'Hello GIT from y'

url = 'https://notify-api.line.me/api/notify'
token ='h8MKeseoDbKeXyo0sofRbhpw6EhBhHLfXRl9pWv7XGH'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

r = requests.post(url, headers=headers, data = {'message':msg})
print (r.text)