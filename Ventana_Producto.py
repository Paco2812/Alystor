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

        self.centrar_ventana(ANCHO, ALTO)

        frame = ct.CTkFrame(self, fg_color="#D3E0F2", width=664, height=362, corner_radius=30)
        frame.place(relx=0.5, rely=0.54, anchor="center")
        frame.grid_propagate(False)

    
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

if __name__ == "__main__":
    app = VentanaProducto()
    app.mainloop()