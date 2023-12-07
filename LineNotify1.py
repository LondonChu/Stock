#裝套件 : $pip install requests
import requests
url = 'https://notify-api.line.me/api/notify'
# 設定權杖 : 登入https://notify-bot.line.me/zh_TW/
貴婦夢token = 'gvLL3yd96E6IJb1VmriRcerD0ARum5aT4z5AqlorVdR'
headers = {
    'Authorization': 'Bearer ' + 貴婦夢token    
}
# 設定要發送的訊息
data = {
    'message':'阿 但是看不到你回的'#,
    'stickerPackageId':'6136',
    'stickerId':'10551397'
}
data = requests.post(url, headers=headers, data=data)