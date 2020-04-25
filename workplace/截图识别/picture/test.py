from PIL import ImageGrab, Image
from xlutils.copy import copy
import pytesseract
import xlwt
import xlrd


# bbox = (200, 200, 400, 400)
# im = ImageGrab.grab(bbox)
# im.save(r'workplace\截图识别\picture\jt.png')



bbox = (200, 200, 400, 400)
im = ImageGrab.grab(bbox)
im.save(r'workplace\截图识别\picture\jietu.jpg')