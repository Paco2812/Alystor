import qrcode
import os

def generar_qr(url, nombre):
    ruta = "media/qr"
    os.makedirs(ruta, exist_ok=True)

    img = qrcode.make(url)
    archivo = os.path.join(ruta, f"{nombre}.png")
    img.save(archivo)

    return archivo
