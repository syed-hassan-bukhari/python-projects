import os
import qrcode

# Ensure the folder exists
os.makedirs("static", exist_ok=True)

print("https://music.youtube.com/watch?v=ppcVqfsekIs&list=RDAMVMX5aBuIDhWHk")
s = input()

q = qrcode.QRCode(version=1, box_size=10, border=5)
q.add_data(s)
q.make(fit=True)

img = q.make_image(fill="black", back_color="white")
img.save("static/qrcode.jpg")

print("✅ QR Code saved as static/qrcode.jpg")
