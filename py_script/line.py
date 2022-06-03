
import requests
# LINE notify
url = 'https://notify-api.line.me/api/notify'
token = ''
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = 'ทดสอบการแจ้งเตือน'
r = requests.post(url, headers=headers, data = {'message':msg})
print(r.text)
