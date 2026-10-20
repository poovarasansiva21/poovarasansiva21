# Turns the white-background photo into a transparent PNG/WebP cut-out
import numpy as np, base64, io
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
im = Image.open('/mnt/user-data/uploads/1792476510982_image.png').convert('RGB')
a = np.array(im).astype(int)
near_white = a.min(axis=2) >= 236
lab, n = ndi.label(near_white)
border = set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]]))) - {0}
bg = np.isin(lab, list(border))
bg = ndi.binary_dilation(bg, iterations=1)           # kill white fringe
alpha = Image.fromarray(((~bg)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.1))
out = im.convert('RGBA'); out.putalpha(alpha)
bbox = alpha.point(lambda v: 255 if v>128 else 0).getbbox()
x0,y0,x1,y1 = bbox; pad=14
out = out.crop((max(0,x0-pad), max(0,y0-pad), min(out.width,x1+pad), out.height))
h=860; out = out.resize((int(out.width*h/out.height), h), Image.LANCZOS)
buf = io.BytesIO(); out.save(buf,'WEBP',quality=86,method=6)
open('portrait.b64','w').write(base64.b64encode(buf.getvalue()).decode())
out.save('portrait-preview.png')
print(out.size, len(buf.getvalue())//1024,'KB')
