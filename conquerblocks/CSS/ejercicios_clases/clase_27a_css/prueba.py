import tkinter as tk

def on_click(event):
    event.widget.config(bg="#FF0000")  # Rojo al hacer clic

root = tk.Tk()

boton = tk.Button(root, 
                 text='Botón', 
                 bg="#0000FF",           # Color base azul
                 activebackground="#000080",  # Color azul oscuro para hover
                 fg="white", 
                 activeforeground="white",    # Color del texto durante hover
                 width=20, 
                 height=2)
boton.pack()

boton.bind("<Button-1>", on_click)  

root.mainloop()
