import os
import qrcode
from PIL import Image
from pyzbar import pyzbar


def decode_qr_code(code_img_path):
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)

    # Here, set only recognize QR Code and ignore other type of code
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])


result = decode_qr_code("1.png")
if len(result):
    for i in range (len(result)):
        print(result[i])
    print(result[0].data.decode("utf-8"))
