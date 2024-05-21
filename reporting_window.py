from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
import sqlite3

# Crear la segunda ventana de manejo de usuarios
class Reporting(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()

        layout = QVBoxLayout()

        # Crear y añadir los botones al diseño
        botones = [
            ("Sales reports", self.sales_reports),
            ("Inventory reports", self.inventory_reports),
            ("User activity reports", self.user_act_reports)
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.boton_regresar = QPushButton("Regresar al menú anterior")
        self.boton_regresar.clicked.connect(menu_anterior)
        
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)

        self.setWindowTitle('Reports')
        self.show()

    def sales_reports(self):
        # Add user functionality
        pass

    def inventory_reports(self):
        # Edit user functionality
        pass

    def user_act_reports(self):
        # View users functionality
        pass


