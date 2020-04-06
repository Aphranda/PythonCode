from PIL import Image
from pyzbar import pyzbar



def identify():
    im = Image.open(r'hacker\picture\二维码.jpg')
    data = pyzbar.decode(im)
    print(data)


if __name__ == "__main__":
    identify()