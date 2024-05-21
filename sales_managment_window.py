from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
import sqlite3

# Crear la segunda ventana de manejo de usuarios
class SalesManagment(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()

        layout = QVBoxLayout()

        # Crear y añadir los botones al diseño
        botones = [
            ("Record Sale", self.record_sale),
            ("View Sales", self.view_sales)
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.boton_regresar = QPushButton("Regresar al menú anterior")
        self.boton_regresar.clicked.connect(menu_anterior)
        
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

        self.setWindowTitle('Sales Managment')
        self.show()

    def record_sale(self):
        # Add user functionality
        pass

    def view_sales(self):
        # Edit user functionality
        pass


