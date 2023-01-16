import pyqrcode
import png
link = "https://www.linkedin.com/in/harshal-bordiya-1b868418b"
qr_code = pyqrcode.create(link)
print (qr_code.png("linkedin.png", scale=5))