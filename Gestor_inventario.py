import customtkinter as ct
from PIL import Image

class VentanaInventario(ct.CTk):
    def __init__(self):
        super().__init__()

        self.imagenes_cache = []

        self.productos = [
            ('Agua Ciel 600ml', 'Productos/Ciel_600.png', 'QR.png', 'Optimo'),
            ('Agua Ciel 1l', 'Productos/Ciel_1L.png', 'QR.png', 'Optimo'),
            ('Coca Cola 600ml', 'Productos/CocaCola_600.png', 'QR.png', 'Agotado'),
            ('Fanta Naranja 600ml', 'Productos/Fanta_Naranja_600.png', 'QR.png', 'Critico'),
            ('Fanta Uva 600ml', 'Productos/Fanta_Uva_600.png','QR.png', 'Optimo'),
            ('Agua Ciel 1l', 'Productos/Ciel_1L.png', 'QR.png', 'Optimo'),
            ('Coca Cola 600ml', 'Productos/CocaCola_600.png', 'QR.png', 'Agotado'),
            ('Fanta Naranja 600ml', 'Productos/Fanta_Naranja_600.png', 'QR.png', 'Critico'),
            ('Fanta Uva 600ml', 'Productos/Fanta_Uva_600.png','QR.png', 'Optimo'),
            ('Agua Ciel 1l', 'Productos/Ciel_1L.png', 'QR.png', 'Optimo'),
            ('Coca Cola 600ml', 'Productos/CocaCola_600.png', 'QR.png', 'Agotado'),
            ('Fanta Naranja 600ml', 'Productos/Fanta_Naranja_600.png', 'QR.png', 'Critico'),
            ('Fanta Uva 600ml', 'Productos/Fanta_Uva_600.png','QR.png', 'Optimo'),
            ('Sprite 600ml', 'Productos/Sprite_600.png', 'QR.png', 'Excesivo')
        ]

        ct.set_appearance_mode("light") 
        self.configure(fg_color="#78A4E1")
        self.title("Gestor de Inventario")

        ANCHO = 725
        ALTO = 450
        self.centrar_ventana(ANCHO, ALTO)

        frame = ct.CTkScrollableFrame(self, fg_color="#D3E0F2", width=664, height=362, corner_radius=30)
        frame.place(relx=0.5, rely=0.54, anchor="center")

        self.lista_productos(frame)

    def centrar_ventana(self, ancho, alto):
        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def cargar_imagen(self, ruta, ancho, alto):
        imagen = Image.open(ruta)
        imagen = imagen.resize((ancho, alto))
        return ct.CTkImage(imagen)


    def crear_frame_productos(self, frame, fila, nombre, imagen, qr, estado):
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
        frame_producto.grid(row=fila, column=0, padx=30, pady=5)

        img1 = self.cargar_imagen(imagen, 30, 30)
        self.imagenes_cache.append(img1)
        label_imagen = ct.CTkLabel(frame_producto, image=img1, text="")
        label_imagen.grid(row=0, column=0, padx=5, pady=5)

        label_nombre = ct.CTkLabel(frame_producto, text=nombre, fg_color="transparent", font=("Arial", 16))
        label_nombre.grid(row=0, column=1, padx=5, pady=5)

        img2 = self.cargar_imagen(qr, 30, 30)
        self.imagenes_cache.append(img2)
        label_qr = ct.CTkLabel(frame_producto, image=img2, text="")
        label_qr.grid(row=0, column=2, padx=30, pady=5)

        return frame_producto
    
    def lista_productos(self, frame):
        n=0
        for producto in self.productos:
            self.crear_frame_productos(frame, n, producto[0], producto[1], producto[2], producto[3])
            n += 1

        return

if __name__ == "__main__":
    app = VentanaInventario()
    app.mainloop()
