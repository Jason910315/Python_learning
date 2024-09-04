import cv2
import time
# 來源串流網址
url = 'https://cctv6.kctmc.nat.gov.tw/f6ad1a36/'
cap = cv2.VideoCapture(url)             #讀取來源

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True: #不斷更新畫面
    ret, frame = cap.read()             #會讀取畫面，其中ret代表是否讀取成功(bool值)，frame為每一偵圖片
    if not ret:
        print("Cannot receive frame")   #如果讀取錯誤，印出訊息
        cap = cv2.VideoCapture(url)     #有時候串流間隔時間較久會中斷，中斷時重新讀取
        continue
    
    cv2.imshow('Kaohsiung', frame) #如果讀取成功，顯示該幀的畫面
    key = cv2.waitKey(100) #在給定的時間內監聽鍵盤事件
    if key == ord('q'): #按下q離開
        break
    if key == ord('a'): #按下a儲存影像，以當下時間為檔名
        cv2.imwrite(f'test{time.time_ns()}.jpg',frame) 

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗