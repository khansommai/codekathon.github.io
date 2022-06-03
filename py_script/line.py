
import requests
# LINE notify
url = 'https://notify-api.line.me/api/notify'
token = 'vsz5C3DmtRC3L8dWQ0Y2TGDRy3HB13DSj4ajwUSNhPF'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = 'ทดสอบการแจ้งเตือน'
r = requests.post(url, headers=headers, data = {'message':msg})
print(r.text)
