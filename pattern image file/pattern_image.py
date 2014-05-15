# http://patterns.ava7.com 에서 1080p의 패턴이미지를 다운받아 png 형태로 저장

import urllib.request, time

for count in range(1,301) : #1~300까지 300번 반복
    urllib.request.urlretrieve("http://patterns.ava7.com/download_wallpaper.php?id="+str(count*3)+"&w=1920&h=1080",str(count)+".PNG") # 3배수의 이미지를 선택
    time.sleep(count%7+1) # 아이피 차단을 막기 위하여 매 회수마다 1~7초동안 슬립
