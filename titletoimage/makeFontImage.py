
from PIL import Image, ImageFont, ImageDraw

def makeFontImage(fontType = 'arial.ttf', fontSize = 10, fontColor = 'yellow', string = 'type something'):

    font = ImageFont.truetype(fontType, fontSize)
    fontSizeX, fontSizeY = font.getsize(string)
    transparencyImage = Image.new("RGBA", (fontSize+fontSizeX,fontSize+fontSizeY))
    
    draw = ImageDraw.Draw(transparencyImage)    
    draw.text((int(fontSize/2),int(fontSize/2)), string, fill = fontColor,font = font)
    name = string + '.png'

    transparencyImage.save(name,'PNG')
    

    

    
