from ui.registrar_producto import RegistrarProducto
import customtkinter as ct
from PIL import Image


class VentanaProductos(ct.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
    
        ct.set_appearance_mode("light") 
        
        # Creación de la ventana principal
        self.configure(fg_color="#78A4E1")
        self.title("Información producto")
        ANCHO = 725
        ALTO = 750

        self.centrar_ventana(ANCHO, ALTO)

        frame = RegistrarProducto(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
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
    app = VentanaProductos()
    app.mainloop()