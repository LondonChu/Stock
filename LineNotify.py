#裝套件 : $pip install requests
import requests
url = 'https://notify-api.line.me/api/notify'
# 設定權杖 : 登入https://notify-bot.line.me/zh_TW/
token = 'gvLL3yd96E6IJb1VmriRcerD0ARum5aT4z5AqlorVdR'
headers = {
    'Authorization': 'Bearer ' + token    
}
# 設定要發送的訊息
data = {
    'message':'[華通] 上車!!'
}
data = requests.post(url, headers=headers, data=data)
# 設定要發送的貼圖
data = {
    'message':'貼圖',
    'stickerPackageId':'6370',
    'stickerId':'11088018',
}
data1 = {
    'message':'貼圖',
    'stickerPackageId':'6370',
    'stickerId':'11088037'
}
data = requests.post(url, headers=headers, data=data)
data1 = requests.post(url, headers=headers, data=data1)
# 設定要發送的圖片
data = {
    'message':'圖片',
    'imageThumbnail':'https://4.bp.blogspot.com/-rwOJYDsjhoE/WgzoiVvJFaI/AAAAAAAKLfw/YDnLgPuTlRUhUkzXAcxdVHVVyEyyxBY_ACLcBGAs/s1600/AS003312_03.gif',
    'imageFullsize':'https://4.bp.blogspot.com/-rwOJYDsjhoE/WgzoiVvJFaI/AAAAAAAKLfw/YDnLgPuTlRUhUkzXAcxdVHVVyEyyxBY_ACLcBGAs/s1600/AS003312_03.gif'
}
data = requests.post(url, headers=headers, data=data)

#Ref : https://steam.oxxostudio.tw/category/python/spider/line-notify.html