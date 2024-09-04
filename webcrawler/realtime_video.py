import cv2
import time
url = 'https://cctv6.kctmc.nat.gov.tw/f6ad1a36/'
cap = cv2.VideoCapture(url)
init = False
if not cap.isOpened():
    print('Camera is not open')
    exit()
while True:
    ret,frame = cap.read()
    if not init:
        init = True
        w = frame.shape[0]
        h = frame.shape[1]
        cc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter('output.mp4',cc,10.0,(w,h))
    out.write(frame)
    print('ok')
    key = cv2.waitKey(100)
    if key == ord('q'):                 # 每一毫秒更新一次，直到按下 q 結束
        break
    elif key == ord('a'):               # 按下 a 儲存當下影格
        cv2.imwrite(f'test{time.time_ns()}.jpg', frame)  # 存成 jpg，取得當下時間作為檔名
    cv2.imshow('oxxostudio', frame)     # 如果讀取成功，顯示該幀的畫面

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗