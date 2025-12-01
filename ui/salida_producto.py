import customtkinter as ctk
from controllers.productos_controller import registrar_salida

class SalidaProducto(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Registrar Salida 🚚", font=("Arial", 22)).pack(pady=10)

        self.id_lote = ctk.CTkEntry(self, placeholder_text="ID del lote")
        self.id_lote.pack(pady=5)

        self.cantidad = ctk.CTkEntry(self, placeholder_text="Cantidad a retirar")
        self.cantidad.pack(pady=5)

        self.mensaje = ctk.CTkLabel(self, text="")
        self.mensaje.pack(pady=5)

        btn = ctk.CTkButton(self, text="Confirmar salida", command=self.salida)
        btn.pack(pady=10)

    def salida(self):
        try:
            registrar_salida(int(self.id_lote.get()), int(self.cantidad.get()))
            self.mensaje.configure(text="✅ Salida registrada", text_color="green")
        except Exception as e:
            self.mensaje.configure(text=str(e), text_color="red")
