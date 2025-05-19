# view/interfaz_cliente.py

import customtkinter as ctk
from tkinter import messagebox

class InterfazCliente:
    def __init__(self, root, controlador):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = root
        self.controlador = controlador

        self.root.title("Atención al Cliente")
        self.root.geometry("400x300")

        ctk.CTkLabel(root, text="Bienvenido al Banco", font=("Arial Bold", 18)).pack(pady=10)

        ctk.CTkLabel(root, text="Nombre:").pack(pady=5)
        self.entry_nombre = ctk.CTkEntry(root)
        self.entry_nombre.pack(pady=5)

        ctk.CTkLabel(root, text="DNI:").pack(pady=5)
        self.entry_dni = ctk.CTkEntry(root)
        self.entry_dni.pack(pady=5)

        ctk.CTkLabel(root, text="Consulta:").pack(pady=5)
        self.combo_consulta = ctk.CTkOptionMenu(root, values=["Transferencia", "Retiro", "Trámite", "Préstamo", "Otros"])
        self.combo_consulta.pack(pady=5)

        ctk.CTkButton(root, text="Generar Consulta", command=self.enviarConsulta).pack(pady=20)

    def enviarConsulta(self):
        nombre = self.entry_nombre.get()
        dni = self.entry_dni.get()
        consulta = self.combo_consulta.get()

        if not nombre or not dni or not consulta:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return
        if len(dni) != 8 or not dni.isdigit():
            messagebox.showerror("Error", "El DNI debe tener exactamente 8 dígitos.")
            return

        cliente = self.controlador.recibirCliente("normal")
        self.controlador.asignarDatosCliente(cliente, {
            "nombre": nombre,
            "dni": dni,
            "consulta": consulta
        })

        messagebox.showinfo("Consulta Generada", f"Cliente {cliente} registrado.")
        self.root.destroy()
