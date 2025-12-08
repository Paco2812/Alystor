import customtkinter as ct
from PIL import Image
from Ventana_Producto import VentanaProducto

class VentanaInventario(ct.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)


        self.imagenes_cache = []

        self.productos = [
            ('Agua Ciel 600ml', 'Productos/Ciel_600.png', 'img_iconos/QR.png', 'Optimo'),
            ('Agua Ciel 1l', 'Productos/Ciel_1L.png', 'img_iconos/QR.png', 'Optimo'),
            ('Coca Cola 600ml', 'Productos/CocaCola_600.png', 'img_iconos/QR.png', 'Agotado'),
            ('Fanta Naranja 600ml', 'Productos/Fanta_Naranja_600.png', 'img_iconos/QR.png', 'Critico'),
            ('Fanta Uva 600ml', 'Productos/Fanta_Uva_600.png','img_iconos/QR.png', 'Optimo'),
            ('Agua Ciel 1l', 'Productos/Ciel_1L.png', 'img_iconos/QR.png', 'Optimo'),
            ('Coca Cola 600ml', 'Productos/CocaCola_600.png', 'img_iconos/QR.png', 'Agotado'),
            ('Fanta Naranja 600ml', 'Productos/Fanta_Naranja_600.png', 'img_iconos/QR.png', 'Critico'),
            ('Fanta Uva 600ml', 'Productos/Fanta_Uva_600.png','img_iconos/QR.png', 'Optimo'),
            ('Agua Ciel 1l', 'Productos/Ciel_1L.png', 'img_iconos/QR.png', 'Optimo'),
            ('Coca Cola 600ml', 'Productos/CocaCola_600.png', 'img_iconos/QR.png', 'Agotado'),
            ('Fanta Naranja 600ml', 'Productos/Fanta_Naranja_600.png', 'img_iconos/QR.png', 'Critico'),
            ('Fanta Uva 600ml', 'Productos/Fanta_Uva_600.png','img_iconos/QR.png', 'Optimo'),
            ('Sprite 600ml', 'Productos/Sprite_600.png', 'img_iconos/QR.png', 'Excesivo')
        ]

        ct.set_appearance_mode("light") 
        self.configure(fg_color="#78A4E1")
        self.title("Gestor de Inventario")

        ANCHO = 725
        ALTO = 450

        MARGEN_X = 56
        MARGEN_Y = 72

        ANCHO_SCROLL = ANCHO - (MARGEN_X * 2)
        ALTO_SCROLL = ALTO - (MARGEN_Y * 2)

        self.centrar_ventana(ANCHO, ALTO)

        frame = ct.CTkScrollableFrame(self, fg_color="#D3E0F2", width=ANCHO_SCROLL, height=ALTO_SCROLL, corner_radius=30)
        frame.place(relx=0.5, rely=0.54, anchor="center")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)
        frame.grid_columnconfigure(2, weight=1)

        self.lista_productos(frame)

    def centrar_ventana(self, ancho, alto):
        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def cargar_imagen(self, ruta, ancho, alto):
        img = Image.open(ruta)
        img = img.resize((ancho, alto))
        return ct.CTkImage(light_image=img, dark_image=img, size=(ancho, alto))


    def crear_frame_productos(self, frame, fila, nombre, imagen, qr, estado, comando=None):
        color = ""
        if (estado == "Excesivo"):
            color = "#A791FF"
        elif (estado == "Optimo"):
            color = "#91FFAB"
        elif (estado == "Critico"):
            color = "#FFFD8A"    
        elif (estado == "Agotado"):
            color = "#FF8080"    

        frame_producto = ct.CTkFrame(frame, fg_color=color, width=600, height=40)
        frame_producto.grid(row=fila, column=1, pady=5, sticky="nsew")
        frame_producto.grid_propagate(False)

        frame_producto.grid_columnconfigure(1, weight=1)

        img1 = self.cargar_imagen(imagen, 30, 30)
        self.imagenes_cache.append(img1)
        label_imagen = ct.CTkLabel(frame_producto, image=img1, text="")
        label_imagen.grid(row=0, column=0, padx=5, pady=5)

        label_nombre = ct.CTkLabel(frame_producto, text=nombre, fg_color="transparent", font=("Arial", 16))
        label_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        label_estado = ct.CTkLabel(frame_producto, text=estado, fg_color="transparent", font=("Arial", 16))
        label_estado.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        img2 = self.cargar_imagen(qr, 30, 30)
        self.imagenes_cache.append(img2)
        label_qr = ct.CTkLabel(frame_producto, image=img2, text="")
        label_qr.grid(row=0, column=3, padx=30, pady=5, sticky="e")

        frame_producto.bind("<Button-1>", lambda e: comando())
        label_imagen.bind("<Button-1>", lambda e: comando())
        label_nombre.bind("<Button-1>", lambda e: comando())
        label_qr.bind("<Button-1>", lambda e: comando())

        return frame_producto
    
    def lista_productos(self, frame):
        n=0
        for producto in self.productos:
            self.crear_frame_productos(frame, n, producto[0], producto[1], producto[2], producto[3], self.abrir_info_producto)
            n += 1

        return

    def abrir_info_producto(self, event=None):
        ventana_producto = VentanaProducto(self)
        ventana_producto.grab_set()

if __name__ == "__main__":
    app = VentanaInventario()
    app.mainloop()
