import customtkinter as ctk
from tkinter import messagebox
from view.interfaz_admin import InterfazAdmin
from view.interfaz_cliente import InterfazCliente

def mostrarLogin(gestor_usuarios, gestor_banco, gestor_clientes):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Login")
    root.geometry("400x250")

    frame = ctk.CTkFrame(root, corner_radius=15)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    ctk.CTkLabel(frame, text="Usuario").pack(pady=5)
    entry_usuario = ctk.CTkEntry(frame)
    entry_usuario.pack(pady=5)

    ctk.CTkLabel(frame, text="Contraseña").pack(pady=5)
    entry_contra = ctk.CTkEntry(frame, show="*")
    entry_contra.pack(pady=5)

    def login():
        usuario = entry_usuario.get()
        contra = entry_contra.get()

        datos = {"usuario": usuario, "contraseña": contra}
        usuario_autenticado = gestor_usuarios.autenticarUsuario(datos)

        if usuario_autenticado:
            root.destroy()
            nueva = ctk.CTk()
            if usuario_autenticado.usuario == "admin":
                InterfazAdmin(nueva, gestor_banco)  
            else:
                InterfazCliente(nueva, gestor_clientes)  
            nueva.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    ctk.CTkButton(frame, text="Ingresar", command=login).pack(pady=20)
    root.mainloop()
