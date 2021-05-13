import stepic
from PIL import Image

class Steg:
    def __init__(self):
        pass

    def bintext(self,text):
        return bytes(text,'utf-8')

    def encode(self,img,t):
        original = Image.open(img)
        encoded = stepic.encode(original,self.bintext(t))
        encoded.save(img,'PNG')

    def decode(self,img):
        original = Image.open(img)
        decoded = stepic.decode(original)
        print(decoded)

if __name__ == '__main__':
    S = Steg()
    S.encode('tesla.png','Mahanth')
    S.decode('tesla.png')