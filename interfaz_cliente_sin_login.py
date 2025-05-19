import customtkinter as ctk
from tkinter import messagebox

class InterfazClienteSinLogin:
    def __init__(self, root, gestor_clientes):
        self.root = root
        self.gestor_clientes = gestor_clientes

        self.root.title("Cliente sin Login - Generar Ticket")
        self.root.geometry("400x350")

        frame = ctk.CTkFrame(root, corner_radius=15)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Ingrese su DNI:").pack(pady=5)

        # Función para permitir solo números y máximo 8 dígitos
        def solo_digitos(text):
            return text.isdigit() and len(text) <= 8 or text == ""

        # Registrar la validación para Tkinter
        vcmd = self.root.register(solo_digitos)
        self.entry_dni = ctk.CTkEntry(frame, validate="key", validatecommand=(vcmd, "%P"))
        self.entry_dni.pack(pady=5)

        ctk.CTkLabel(frame, text="Seleccione trámite:").pack(pady=5)
        self.combo_tramite = ctk.CTkComboBox(frame, values=["Consulta", "Trámite", "Pago", "Otros"])
        self.combo_tramite.pack(pady=5)
        self.combo_tramite.set("Consulta")

        self.btn_generar = ctk.CTkButton(frame, text="Generar Ticket", command=self.generar_ticket)
        self.btn_generar.pack(pady=15)

        self.label_ticket = ctk.CTkLabel(frame, text="")
        self.label_ticket.pack(pady=5)
        self.label_ventanilla = ctk.CTkLabel(frame, text="")
        self.label_ventanilla.pack(pady=5)
        self.label_espera = ctk.CTkLabel(frame, text="")
        self.label_espera.pack(pady=5)

    def generar_ticket(self):
        dni = self.entry_dni.get().strip()
        tramite = self.combo_tramite.get()

        # Validación final de DNI antes de generar ticket
        if len(dni) != 8 or not dni.isdigit():
            messagebox.showerror("Error", "El DNI debe tener exactamente 8 dígitos.")
            return

        ticket = self.gestor_clientes.generar_ticket(dni, tramite)

        if ticket is None:
            messagebox.showerror("Error", "Hubo un problema al generar el ticket.")
            return

        texto_ticket = f"Ticket generado: {ticket['codigo']}"
        texto_ventanilla = f"Ventanilla asignada: {ticket['ventanilla']}"
        texto_espera = f"Tiempo estimado de espera: {ticket['espera']} minutos"

        self.label_ticket.configure(text=texto_ticket)
        self.label_ventanilla.configure(text=texto_ventanilla)
        self.label_espera.configure(text=texto_espera)
