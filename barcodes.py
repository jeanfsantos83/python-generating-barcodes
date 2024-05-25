# pip install python-barcode #
from barcode import EAN13
from barcode.writer import ImageWriter

# Generates the barcode and saves it to the desired path #
with open(r'C:\Users\makig\Documents\Scripts-Python\python-barcodes\barcode.png', 'wb') as f:
    EAN13('123456789102', writer=ImageWriter()).write(f)
