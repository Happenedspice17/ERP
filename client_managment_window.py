from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
import sqlite3

# Crear la segunda ventana de manejo de usuarios
class ClientManagment(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()

        layout = QVBoxLayout()

        # Crear y añadir los botones al diseño
        botones = [
            ("Add Client", self.add_client),
            ("Edit Client", self.edit_client),
            ("View Clients", self.view_clients),
            ("Delete Client", self.delete_client),
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.boton_regresar = QPushButton("Regresar al menú anterior")
        self.boton_regresar.clicked.connect(menu_anterior)
        
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('Client Managment')
        self.show()

    def add_client(self):
        # Add user functionality
        pass

    def edit_client(self):
        # Edit user functionality
        pass

    def view_clients(self):
        # View users functionality
        pass

    def delete_client(self):
        # Delete user functionality
        pass

