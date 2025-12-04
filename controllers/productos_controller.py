from database.db import Session
from database.models import Categoria, Producto, Lote, Ubicacion, MovimientoInventario
from datetime import datetime, date
from sqlalchemy.orm import joinedload
from services.barcode_service import generar_codigo_barras
from services.qr_service import generar_qr

#IP_LOCAL = "192.168.100.64"
IP_LOCAL = "10.61.212.161"


def registrar_producto(data):
    session = Session()

    # VALIDACIONES
    if not data["nombre"] or not data["lote"]:
        raise ValueError("Nombre y lote son obligatorios")

    if int(data["cantidad"]) <= 0:
        raise ValueError("Cantidad inválida")

    # FECHAS
    fecha_ingreso = data["fecha_ingreso"]
    fecha_caducidad = data["caducidad"]

    # fecha_ingreso
    if isinstance(fecha_ingreso, str):
        fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()

    # fecha_caducidad (opcional)
    if fecha_caducidad:
        fecha_caducidad = datetime.strptime(fecha_caducidad, "%Y-%m-%d").date()
    else:
        fecha_caducidad = None


    # CATEGORIA
    categoria = session.query(Categoria).filter_by(nombre=data["categoria"]).first()
    if not categoria:
        categoria = Categoria(nombre=data["categoria"])
        session.add(categoria)
        session.commit()


    codigo_unico = f"ALY-{int(datetime.now().timestamp())}"
    ruta_barcode = generar_codigo_barras(codigo_unico)

    # PRODUCTO
    producto = session.query(Producto).filter_by(nombre=data["nombre"]).first()
    if not producto:
        producto = Producto(
            nombre=data["nombre"],
            categoria=categoria,
            codigo_barras=codigo_unico,
            codigo_qr="PENDIENTE"
        )
        session.add(producto)
        session.commit()   # 👈 aquí se genera el ID

        url = f"http://{IP_LOCAL}:5001/producto/{producto.id_producto}"
        ruta_qr = generar_qr(url, producto.codigo_barras)

        producto.codigo_qr = ruta_qr
        session.commit()


        ruta_qr = generar_qr(url, producto.codigo_barras)
        producto.codigo_qr = ruta_qr
        session.add(producto)
        session.commit()
        session.close()
        return ruta_barcode, ruta_qr


    # UBICACION
    ubicacion = session.query(Ubicacion).filter_by(nombre=data["ubicacion"]).first()
    if not ubicacion:
        ubicacion = Ubicacion(nombre=data["ubicacion"])
        session.add(ubicacion)
        session.commit()

    # Validar si el lote ya existe para ese producto
    lote_existente = session.query(Lote).filter_by(
        numero_lote=data["lote"],
        id_producto=producto.id_producto
    ).first()

    if lote_existente:
        raise ValueError("Este lote ya fue registrado para ese producto")
    # LOTE
    lote = Lote(
        numero_lote=data["lote"],
        fecha_ingreso=fecha_ingreso,
        fecha_caducidad=fecha_caducidad,
        cantidad=int(data["cantidad"]),
        unidad=data["unidad"],
        producto=producto,
        ubicacion=ubicacion
    )

    session.add(lote)
    session.commit()
    session.close()

valor = "ALY-1730954123"
#Buscar
def buscar_producto(valor):
    session = Session()
    producto = session.query(Producto).filter(
        (Producto.nombre.ilike(f"%{valor}%")) |
        (Producto.codigo_barras == valor)
    ).all()
    session.close()
    return producto

#Listar Inventario Completo
def obtener_inventario():
    session = Session()

    lotes = (
        session.query(Lote)
        .options(
            joinedload(Lote.producto),
            joinedload(Lote.ubicacion)
        )
        .all()
    )

    session.close()
    return lotes

#Registrar Entrada
def registrar_entrada(id_lote, cantidad):
    if cantidad <= 0:
        raise ValueError("Cantidad inválida")


    session = Session()
    lote = session.get(Lote, id_lote)

    if not lote:
        raise ValueError("Lote no encontrado")

    lote.cantidad += cantidad

    movimiento = MovimientoInventario(
        tipo="ENTRADA",
        cantidad=cantidad,
        lote=lote
    )

    session.add(movimiento)
    session.commit()
    session.close()

#Registrar Salida
def registrar_salida(id_lote, cantidad):
    if cantidad <= 0:
        raise ValueError("Cantidad inválida")


    session = Session()
    lote = session.get(Lote, id_lote)

    if not lote:
        raise ValueError("Lote no encontrado")

    if lote.cantidad < cantidad:
        raise ValueError("Stock insuficiente")

    lote.cantidad -= cantidad

    movimiento = MovimientoInventario(
        tipo="SALIDA",
        cantidad=cantidad,
        lote=lote
    )

    session.add(movimiento)
    session.commit()
    session.close()
    
