from PIL import Image, ImageDraw

img = Image.new('RGB',(100, 100)) #RGB컬러 공간을 가지는 Image 생성

draw = ImageDraw.Draw(img) #Draw객체 생성

draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0)) #Draw Red Ellipse

img.save('TestTransparentPNG.png', 'PNG', transparency=0) #투명한 배경의 png파일로 저장
