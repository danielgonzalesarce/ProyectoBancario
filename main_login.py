import customtkinter as ctk
from tkinter import messagebox
from view.login import mostrarLogin
from view.interfaz_cliente_sin_login import InterfazClienteSinLogin

def ventana_principal(gestor_usuarios, gestor_banco, gestor_clientes):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Sistema Banco - Selección de Perfil")
    root.geometry("400x250")

    frame = ctk.CTkFrame(root, corner_radius=15)
    frame.pack(pady=30, padx=30, fill="both", expand=True)

    ctk.CTkLabel(frame, text="Seleccione su perfil para continuar", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=20)

    def abrir_login_admin_cliente():
        root.destroy()
        mostrarLogin(gestor_usuarios, gestor_banco, gestor_clientes)

    def abrir_cliente_sin_login():
        root.destroy()
        ventana_cliente = ctk.CTk()
        InterfazClienteSinLogin(ventana_cliente, gestor_clientes)
        ventana_cliente.mainloop()

    ctk.CTkButton(frame, text="Administrador / Cliente (Login)", command=abrir_login_admin_cliente).pack(pady=10)
    ctk.CTkButton(frame, text="Cliente (Sacar Ticket y Consultar)", command=abrir_cliente_sin_login).pack(pady=10)

    root.mainloop()
