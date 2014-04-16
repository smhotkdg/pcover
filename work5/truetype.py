from PIL import Image, ImageDraw, ImageFont
'''
트루타입 폰트에 패턴 이미지 합치기 예제
수정요망
1. 트루타입 폰트 이미지 생성시 배경화면 색
2. 트루타입 폰트 이미지의 레이아웃 구성 (예: 타이틀 및 책 정보 폰트 위치)
3. 패턴 이미지 및 트루타입 폰트  종류
4. 타이틀 및 책 정보
5. 클래스 또한 함수화 
'''
pattern_im = Image.open("pattern_image.jpg")
#pattern_im.show()
w,h = pattern_im.size
bg_im = Image.new(mode='RGB', size=(w,h),color=(255,255,254))
font = ImageFont.truetype("Arial.ttf", 200, encoding='unic')
draw = ImageDraw.Draw(bg_im)
line_spacing = draw.textsize('A', font=font)[1] + 50
lines = ['Gwang-Soo Hong', 'Sunmoon Univ.', 'Dept. of Computer Science and Engineering']
y = 0
for line in lines:
    draw.text((0, y), line, font=font)
    y += line_spacing
#bg_im.save('test.png', 'PNG')
for j in range(0,h):
    for i in range(0,w):
        bg_r, bg_g, bg_b = bg_im.getpixel((i,j))
        #print (r,g,b)
        if (bg_r,bg_g,bg_b) != (255,255,254):
            #print (bg_r,bg_b,bg_b)
            pattern_r, pattern_g, pattern_b = pattern_im.getpixel((i,j))
            bg_im.putpixel((i,j),(pattern_r,pattern_g,pattern_b))                
        else:
            pass
bg_im.save("test.png","PNG")
                           
