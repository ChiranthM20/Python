import qrcode

img = qrcode.make("Hello! This is Chiranth M")
img.save("eik_qr.png")
print("QR Code generation successful")