import customtkinter as ct
from PIL import Image
from Gestor_inventario import VentanaInventario

class VentanaPrincipal(ct.CTk):
    def __init__(self):
        super().__init__()
    
        ct.set_appearance_mode("light") 

        # Creación de la ventana principal
        self.configure(fg_color="#78A4E1")
        self.title("Menu Alystor")
        ANCHO = 725
        ALTO = 450

        self.centrar_ventana(ANCHO, ALTO)

        frame = ct.CTkFrame(self, fg_color="#D3E0F2", width=664, height=362, corner_radius=30)
        frame.place(relx=0.5, rely=0.54, anchor="center")
        frame.grid_propagate(False)
        for i in range(2):     # filas 0 y 1
            frame.grid_rowconfigure(i, weight=1)

        for j in range(3):     # columnas 0, 1 y 2
            frame.grid_columnconfigure(j, weight=1)

        # Logo Alystor en el centro del frame
        frame_logo = ct.CTkFrame(frame, fg_color="transparent")
        frame_logo.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", rowspan=2)

        label_logo = self.label_imagen(frame_logo, self.cargar_imagen("Logo_Alystor.png", 200, 200))

        # Botones de la página de inicio
        boton1 = self.boton_imagen(frame, self.cargar_imagen("inventario.png", 70, 70), "Gestión de inventario", 0, 0, comando=self.abrir_inventario)
        boton2 = self.boton_imagen(frame, self.cargar_imagen("reporte_mensual.png", 70, 70), "Reporte mensual", 1, 0)
        boton3 = self.boton_imagen(frame, self.cargar_imagen("estantes.png", 70, 70), "Consultar estantes", 0, 2)
        boton4 = self.boton_imagen(frame, self.cargar_imagen("scanner.png", 70, 70), "Escanear código", 1, 2)

    
    def centrar_ventana(self, ancho, alto):
        self.update_idletasks()

        # Tomar el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular coordenadas para centrar
        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def cargar_imagen(self, ruta, ancho, alto):

        imagen = ct.CTkImage(
            light_image=Image.open(ruta),
            size=(ancho, alto)                              
        )

        return imagen

    def label_imagen(self, frame, imagen):

        label = ct.CTkLabel(frame, image=imagen, text="", fg_color="transparent")
        label.place(relx=0.5, rely=0.5, anchor="center")

        return label

    def boton_imagen(self, frame, imagen, texto, fila, columna, comando=None):

        frame_boton = ct.CTkFrame(frame, fg_color="transparent")
        frame_boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

        label_img = ct.CTkLabel(frame_boton, image=imagen, text="", fg_color="transparent")
        label_img.pack(pady=(10, 5))

        # Texto debajo
        label_txt = ct.CTkLabel(frame_boton, text=texto, font=("Arial", 14), fg_color="transparent")
        label_txt.pack()

        # Bind para que todo el frame funcione como botón
        frame_boton.bind("<Button-1>", lambda e: comando())
        label_img.bind("<Button-1>", lambda e: comando())
        label_txt.bind("<Button-1>", lambda e: comando())


        return frame_boton
    
    def abrir_inventario(self, event=None):
        ventana_inventario = VentanaInventario(self)
        ventana_inventario.grab_set()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()