# view/interfaz_admin.py

import customtkinter as ctk
from tkinter import messagebox

class InterfazAdmin:
    def __init__(self, root, controlador):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = root
        self.root.title("Gestión de Colas del Banco - Admin")
        self.root.geometry("750x600")
        self.controlador = controlador

        self.tipoCliente = ctk.StringVar(value="normal")

        titulo = ctk.CTkLabel(root, text="Sistema de Gestión de Colas - Banco (Admin)", font=("Arial Bold", 20))
        titulo.pack(pady=10)

        form_frame = ctk.CTkFrame(root, corner_radius=15)
        form_frame.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(form_frame, text="Tipo de Cliente:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="e")

        opciones = ["discapacitado", "vip", "normal"]
        self.comboTipo = ctk.CTkOptionMenu(form_frame, values=opciones, variable=self.tipoCliente)
        self.comboTipo.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkButton(form_frame, text="Agregar Cliente", command=self.agregarCliente, width=200).grid(row=1, column=0, columnspan=2, pady=8)
        ctk.CTkButton(form_frame, text="Ingresar Clientes al Banco", command=self.ingresarClientes, width=200).grid(row=2, column=0, columnspan=2, pady=8)
        ctk.CTkButton(form_frame, text="Enviar a Ventanilla", command=self.atenderClientes, width=200).grid(row=3, column=0, columnspan=2, pady=8)
        ctk.CTkButton(form_frame, text="Finalizar Atención", command=self.finalizarAtencion, width=200).grid(row=4, column=0, columnspan=2, pady=8)

        # === ESTADO DEL BANCO ===
        estado_frame = ctk.CTkFrame(root, corner_radius=15)
        estado_frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(estado_frame, text="Estado Actual del Banco", font=("Arial", 16, "bold")).pack(pady=10)

        self.estado = ctk.CTkTextbox(estado_frame, width=700, height=300, corner_radius=10, font=("Courier New", 13))
        self.estado.pack(padx=10, pady=10, fill="both", expand=True)
        self.estado.configure(state="disabled")

        self.actualizarEstado()

    def agregarCliente(self):
        def guardar_datos():
            nombre = entry_nombre.get()
            dni = entry_dni.get()
            consulta = combo_consulta.get()

            if not nombre or not dni or not consulta:
                messagebox.showerror("Error", "Por favor, completa todos los campos.")
                return
            if len(dni) != 8:
                messagebox.showerror("Error", "El DNI debe tener exactamente 8 dígitos.")
                return

            tipo = self.tipoCliente.get()
            cliente = self.controlador.recibirCliente(tipo)
            self.controlador.asignarDatosCliente(cliente, {
                "nombre": nombre,
                "dni": dni,
                "consulta": consulta
            })

            self.actualizarEstado()
            ventana.destroy()
            messagebox.showinfo("Cliente agregado", f"Cliente {cliente} agregado correctamente.")

        # Ventana emergente para ingresar datos del cliente
        ventana = ctk.CTkToplevel(self.root)
        ventana.title("Datos del Cliente")
        ventana.geometry("400x300")
        ventana.grab_set()

        ctk.CTkLabel(ventana, text="Nombre:").pack(pady=5)
        entry_nombre = ctk.CTkEntry(ventana)
        entry_nombre.pack(pady=5)

        ctk.CTkLabel(ventana, text="DNI:").pack(pady=5)
        entry_dni = ctk.CTkEntry(ventana)
        entry_dni.pack(pady=5)

        def validar_dni_input(caracter):
            return caracter.isdigit() and len(entry_dni.get() + caracter) <= 8

        validar_cmd = ventana.register(validar_dni_input)
        entry_dni.configure(validate="key", validatecommand=(validar_cmd, "%S"))

        ctk.CTkLabel(ventana, text="Consulta:").pack(pady=5)
        combo_consulta = ctk.CTkOptionMenu(ventana, values=["Transferencia", "Retiro", "Trámite", "Préstamo", "Otros"])
        combo_consulta.pack(pady=5)

        ctk.CTkButton(ventana, text="Guardar", command=guardar_datos).pack(pady=20)

    def ingresarClientes(self):
        self.controlador.ingresarClientes()
        self.actualizarEstado()

    def atenderClientes(self):
        self.controlador.atenderClientes()
        self.actualizarEstado()

    def finalizarAtencion(self):
        cliente = self.controlador.finalizarAtencion()
        if cliente:
            messagebox.showinfo("Cliente Atendido", f"Se ha atendido al cliente: {cliente}")
        else:
            messagebox.showinfo("Atención", "No hay clientes siendo atendidos.")
        self.actualizarEstado()

    def actualizarEstado(self):
        estado = self.controlador.estadoBanco()
        self.estado.configure(state="normal")
        self.estado.delete("1.0", "end")
        for nombre_cola, contenido in estado.items():
            self.estado.insert("end", f"{nombre_cola}:\n{contenido}\n\n")
        self.estado.configure(state="disabled")
