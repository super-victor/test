import qrcode
data = "www.baidu.com"
qr = qrcode.QRCode(
    version=4,  # 二维码的实际大小级别(1 - 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 二维码的容错级别(L,M(默认),Q,H)
    box_size=10,  # 整张二维码图片的大小
    border=5,  # 二维码背景边框宽度
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save('test.png')  # 将图片保存为png(注意其他格式可能会出现问题)
print("OK")
