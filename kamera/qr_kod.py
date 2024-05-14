import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "BRAVO! pronasli ste QR kod!"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('qrkod.png', scale = 6)