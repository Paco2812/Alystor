

from sqlalchemy import (
    Column, Integer, String, Date, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# ------------------ CATEGORIA ------------------
class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, unique=True)
    descripcion = Column(String)

    productos = relationship("Producto", back_populates="categoria")


# ------------------ PRODUCTO ------------------
class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    codigo_barras = Column(String, unique=True)
    codigo_qr = Column(String)
    fecha_registro = Column(DateTime, default=datetime.now)

    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"))
    categoria = relationship("Categoria", back_populates="productos")

    lotes = relationship("Lote", back_populates="producto")


# ------------------ UBICACION ------------------
class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    id_ubicacion = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)

    lotes = relationship("Lote", back_populates="ubicacion")


# ------------------ LOTE ------------------
class Lote(Base):
    __tablename__ = "lotes"

    id_lote = Column(Integer, primary_key=True)
    numero_lote = Column(String, nullable=False)
    fecha_ingreso = Column(Date, nullable=False)
    fecha_caducidad = Column(Date)
    cantidad = Column(Integer, nullable=False)
    unidad = Column(String, nullable=False)

    id_producto = Column(Integer, ForeignKey("productos.id_producto"))
    id_ubicacion = Column(Integer, ForeignKey("ubicaciones.id_ubicacion"))

    producto = relationship("Producto", back_populates="lotes")
    ubicacion = relationship("Ubicacion", back_populates="lotes")

    movimientos = relationship("MovimientoInventario", back_populates="lote")


# ------------------ MOVIMIENTO INVENTARIO ------------------
class MovimientoInventario(Base):
    __tablename__ = "movimientos_inventario"

    id_movimiento = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)  # ENTRADA / SALIDA
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.now)
    observacion = Column(String)

    id_lote = Column(Integer, ForeignKey("lotes.id_lote"))
    lote = relationship("Lote", back_populates="movimientos")
