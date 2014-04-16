from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font = ImageFont.truetype("Arial.ttf",50)

img=Image.new("RGB", (500,800))
draw = ImageDraw.Draw(img)
draw.text((150, 200),"Oliverstone",(0,255,0),font=font)
draw = ImageDraw.Draw(img)
img.save("TestTitleToImage.png","PNG",transparency=0)
