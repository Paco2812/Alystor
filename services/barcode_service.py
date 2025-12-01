import barcode
from barcode.writer import ImageWriter
import os

def generar_codigo_barras(codigo):
    ruta = "media/barcodes"
    os.makedirs(ruta, exist_ok=True)

    barcode_class = barcode.get_barcode_class("code128")
    codigo_barra = barcode_class(codigo, writer=ImageWriter())

    archivo = os.path.join(ruta, codigo)
    codigo_barra.save(archivo)

    return f"{archivo}.png"
