import customtkinter as ct
from PIL import Image

class VentanaProducto(ct.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
    
        ct.set_appearance_mode("light") 
        
        # Creación de la ventana principal
        self.configure(fg_color="#78A4E1")
        self.title("Información producto")
        ANCHO = 725
        ALTO = 450

        MARGEN_X = 56
        MARGEN_Y = 72

        ANCHO_SCROLL = ANCHO - (MARGEN_X * 2)
        ALTO_SCROLL = ALTO - (MARGEN_Y * 2)

        self.centrar_ventana(ANCHO, ALTO)

        frame = ct.CTkScrollableFrame(self, fg_color="#D3E0F2", width=ANCHO_SCROLL, height=ALTO_SCROLL, corner_radius=30)
        frame.place(relx=0.5, rely=0.54, anchor="center")

        # Configurar 3 columnas con pesos iguales
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)

        # Para que el contenido crezca verticalmente
        frame.grid_rowconfigure(0, weight=1)

        #frame.grid_propagate(False)

        #Frame izquierdo
        frame_izquierdo = self.crear_frame(frame, 0, 0, "nw", "#D3E0F2")
        img_producto = self.cargar_imagen(frame_izquierdo, "Productos/Ciel_600.png", 120, 120, 0, 0)
        lb_stock = self.crearLabel(frame_izquierdo, "100 objetos en stock", 16, 1, 0)

        #Frame central
        frame_central = self.crear_frame(frame, 0, 1, "nw", "#D3E0F2")
        frame_central.columnconfigure(0, weight=1)
        lb_codigo = self.crearLabel(frame_central, "F03H2", 30, 0, 0)
        lb_producto = self.crearLabel(frame_central, "Agua Ciel 600ml", 35, 1, 0)
        cuadro_estado = self.cuadro_estado(frame_central, "óptimo", 2, 0)
        descripción = "Agua embotellada de la marca Ciel en presentación de 600 mililitros. Ideal para mantenerse hidratado durante el día."
        lb_descripción = self.crearLabelDescripcion(frame_central, f"Descripción: {descripción}", 16, 3, 0)

        #Frame derecho
        frame_derecho = self.crear_frame(frame, 0, 2, "ne", "#D3E0F2")
        img_codigo_barras = self.cargar_imagen(frame_derecho, "barras.png", 100, 50, 0, 0)
        img_codigo_qr = self.cargar_imagen(frame_derecho, "QR.png", 80, 80, 1, 0)

    
    def centrar_ventana(self, ancho, alto):
        self.update_idletasks()

        # Tomar el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular coordenadas para centrar
        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def crear_frame(self, frame_padre, fila, columna, pegado, color):
        frame = ct.CTkFrame(frame_padre, fg_color=color)
        frame.grid(row=fila, column=columna, sticky=pegado)

        return frame
    
    def cargar_imagen(self, frame, ruta, ancho, alto, fila, columna):

        imagen = ct.CTkImage(
            light_image=Image.open(ruta),
            size=(ancho, alto)                              
        )

        label_img = ct.CTkLabel(frame, image=imagen, text="", fg_color="transparent")
        label_img.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

        return label_img

    def crearLabel(self, frame, texto, tam_letra, fila, columna):
        label = ct.CTkLabel(frame, text=texto, font=("Arial", tam_letra))
        label.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

        return label
    
    def crearLabelDescripcion(self, frame, texto, tam_letra, fila, columna):
        label = ct.CTkLabel(frame, text=texto, font=("Arial", tam_letra), justify="left", wraplength=340)
        label.grid(row=fila, column=columna, sticky="nw", padx=10, pady=5)

        #def ajustar_wrap(event=None):
        #    ancho = frame.winfo_width() - 20
        #    if ancho > 50:  # Para evitar wraplength demasiado pequeño antes de cargar
        #        label.configure(wraplength=ancho)

        #frame.bind("<Configure>", ajustar_wrap)
        
        return label

    def cuadro_estado(self, frame, estado, fila, columna):
        color = ""
        if (estado == "excesivo"):
            color = "#A791FF"
        elif (estado == "óptimo"):
            color = "#91FFAB"
        elif (estado == "critico"):
            color = "#FFFD8A"    
        elif (estado == "agotado"):
            color = "#FF8080"    

        frame_estado = ct.CTkFrame(frame, fg_color=color, width=100, height=40)
        frame_estado.grid(row=fila, column=columna, pady=5, sticky="nsew")
        frame_estado.grid_propagate(False)

        label_estado = ct.CTkLabel(frame_estado, text=f"Inventario {estado}", fg_color="transparent", font=("Arial", 20))
        label_estado.place(relx=0.5, rely=0.5, anchor="center")

        return frame_estado
    
if __name__ == "__main__":
    app = VentanaProducto()
    app.mainloop()