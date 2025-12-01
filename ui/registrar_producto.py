import customtkinter as ctk
from datetime import date
from controllers.productos_controller import registrar_producto
from PIL import Image

class RegistrarProducto(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(self, text="Registrar Producto 📦", font=("Arial", 22)).grid(row=0, column=0, columnspan=2, pady=20)

        # Nombre
        ctk.CTkLabel(self, text="Nombre del producto").grid(row=1, column=0, sticky="w")
        self.nombre = ctk.CTkEntry(self)
        self.nombre.grid(row=1, column=1, sticky="ew")

        # Categoria
        ctk.CTkLabel(self, text="Categoría").grid(row=2, column=0, sticky="w")
        self.categoria = ctk.CTkEntry(self)
        self.categoria.grid(row=2, column=1, sticky="ew")

        # Lote
        ctk.CTkLabel(self, text="Número de lote").grid(row=3, column=0, sticky="w")
        self.lote = ctk.CTkEntry(self)
        self.lote.grid(row=3, column=1, sticky="ew")

        # Cantidad
        ctk.CTkLabel(self, text="Cantidad").grid(row=4, column=0, sticky="w")
        self.cantidad = ctk.CTkEntry(self)
        self.cantidad.grid(row=4, column=1, sticky="ew")

        # Unidad
        ctk.CTkLabel(self, text="Unidad").grid(row=5, column=0, sticky="w")
        self.unidad = ctk.CTkComboBox(self, values=["pzas", "kg", "cajas"])
        self.unidad.set("pzas")
        self.unidad.grid(row=5, column=1, sticky="ew")

        # Caducidad
        ctk.CTkLabel(self, text="Fecha de caducidad (YYYY-MM-DD)").grid(row=6, column=0, sticky="w")
        self.caducidad = ctk.CTkEntry(self)
        self.caducidad.grid(row=6, column=1, sticky="ew")

        # Ubicación
        ctk.CTkLabel(self, text="Ubicación").grid(row=7, column=0, sticky="w")
        self.ubicacion = ctk.CTkEntry(self)
        self.ubicacion.grid(row=7, column=1, sticky="ew")

        # Botón
        btn = ctk.CTkButton(self, text="Registrar ✅", command=self.guardar)
        btn.grid(row=8, column=0, columnspan=2, pady=20)

        self.mensaje = ctk.CTkLabel(self, text="")
        self.mensaje.grid(row=9, column=0, columnspan=2)

    def guardar(self):
        datos = {
            "nombre": self.nombre.get(),
            "categoria": self.categoria.get(),
            "lote": self.lote.get(),
            "cantidad": self.cantidad.get(),
            "unidad": self.unidad.get(),
            "caducidad": self.caducidad.get(),
            "ubicacion": self.ubicacion.get(),
            "fecha_ingreso": date.today()
        }
        #ruta = registrar_producto(datos)
        #self.mostrar_barcode(ruta)
        #self.mostrar_qr(ruta_qr)

        try:
            ruta_barcode, ruta_qr = registrar_producto(datos)

            self.mostrar_barcode(ruta_barcode)
            self.mostrar_qr(ruta_qr)

            self.mensaje.configure(text="✅ Producto registrado correctamente", text_color="green")
        except Exception as e:
            self.mensaje.configure(text=f"❌ Error: {e}", text_color="red")
    
    def mostrar_barcode(self, ruta_barcode):
        img = Image.open(ruta_barcode)
        img = ctk.CTkImage(img, size=(300, 100))
        self.barcode_img = ctk.CTkLabel(self, image=img, text="")
        self.barcode_img.grid(row=10, column=0, columnspan=2, pady=10)
    
    def mostrar_qr(self, ruta_qr):
        img = Image.open(ruta_qr)
        img = ctk.CTkImage(img, size=(150,150))
        self.qr_img = ctk.CTkLabel(self, image=img, text="")
        self.qr_img.grid(row=11, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    app = RegistrarProducto()
    app.mainloop()