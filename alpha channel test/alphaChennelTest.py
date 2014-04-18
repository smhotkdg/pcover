import numpy as np
from PIL import Image,ImageDraw

def alpha_composite(src, dst):
    '''
    Return the alpha composite of src and dst.

    Parameters:
    src -- PIL RGBA Image object
    dst -- PIL RGBA Image object
    '''

    src = np.asarray(src)
    dst = np.asarray(dst)
    out = np.empty(src.shape, dtype = 'float')
    alpha = np.index_exp[:, :, 3:]
    rgb = np.index_exp[:, :, :3]
    src_a = src[alpha]/255.0
    dst_a = dst[alpha]/255.0
    out[alpha] = src_a+dst_a*(1-src_a)
    old_setting = np.seterr(invalid = 'ignore')
    out[rgb] = (src[rgb]*src_a + dst[rgb]*dst_a*(1-src_a))/out[alpha]
    np.seterr(**old_setting)    
    out[alpha] *= 255
    np.clip(out,0,255)
    out = out.astype('uint8')
    out = Image.fromarray(out, 'RGBA')
    return out

img1 = Image.new('RGBA', size = (100, 100), color = (255, 0, 0, 255))
draw = ImageDraw.Draw(img1)
draw.rectangle((33, 0, 66, 100), fill = (255, 0, 0, 128))
draw.rectangle((67, 0, 100, 100), fill = (255, 0, 0, 0))
img1.save('img1.png')

img2 = Image.new('RGBA', size = (100, 100), color = (0, 255, 0, 255))
draw = ImageDraw.Draw(img2)
draw.rectangle((0, 33, 100, 66), fill = (0, 255, 0, 128))
draw.rectangle((0, 67, 100, 100), fill = (0, 255, 0, 0))
img2.save('img2.png')

img3 = alpha_composite(img1, img2)
img3.save('composited_img.png')
