import requests

radar_url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON'
radar = requests.get(radar_url)        # 爬取資料
radar_json = radar.json()              # 使用 JSON 格式
radar_img = radar_json['cwaopendata']['dataset']['resource']['ProductURL']  # 取得圖片網址
print(radar_img)

url = 'https://notify-api.line.me/api/notify'    # LINE Notify API 網址
token = 'PTHEbgxwvAGR0mAVEPLXqYEEcLfDhw3BkPote33fImi'                   # 自己申請的 LINE Notify 權杖
headers = {
    'Authorization': 'Bearer ' + token           # POST 使用的 headers
}
data = {
    'message':'從雷達回波看看會不會下雨～',   # 發送的訊息
    'imageThumbnail':radar_img,          # 預覽圖網址
    'imageFullsize':radar_img            # 完整圖片網址
}
data = requests.post(url, headers=headers, data=data)    # 發送 LINE NOtify