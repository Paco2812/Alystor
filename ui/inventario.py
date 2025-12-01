import customtkinter as ctk
from controllers.productos_controller import obtener_inventario

class Inventario(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Inventario 📋", font=("Arial", 22)).pack(pady=10)

        self.lista = ctk.CTkTextbox(self, height=300)
        self.lista.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_datos()

    def cargar_datos(self):
        self.lista.delete("1.0", "end")
        lotes = obtener_inventario()

        for lote in lotes:
            texto = (
                f"Producto: {lote.producto.nombre}\n"
                f"Lote: {lote.numero_lote}\n"
                f"Cantidad: {lote.cantidad} {lote.unidad}\n"
                f"Ubicación: {lote.ubicacion.nombre}\n"
                f"Caducidad: {lote.fecha_caducidad}\n"
                "-----------------------------\n"
            )
            self.lista.insert("end", texto)
