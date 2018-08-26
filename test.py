from pyzbar.pyzbar import decode
from PIL import Image

def constructor():
    print("\n\n")
    print("------------------------starting---------------------------")

def destructor():
    print("------------------------ending---------------------------")
    print("\n\n")

constructor()
a=decode(Image.open('./test.png'))
print("\n\n")
print(a)

destructor()
