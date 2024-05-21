from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
import sqlite3

# Crear la segunda ventana de manejo de usuarios
class ProductManagment(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()

        layout = QVBoxLayout()

        # Crear y añadir los botones al diseño
        botones = [
            ("Add Product", self.add_product),
            ("Edit Product", self.edit_product),
            ("View Products", self.view_products),
            ("Delete Product", self.delete_product),
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.boton_regresar = QPushButton("Regresar al menú anterior")
        self.boton_regresar.clicked.connect(menu_anterior)
        
        layout.addWidget(self.boton_regresar)

        self.setLayout(layout)
        self.setWindowTitle('Product Managment')
        self.show()

    def add_product(self):
        # Add user functionality
        pass

    def edit_product(self):
        # Edit user functionality
        pass

    def view_products(self):
        # View users functionality
        pass

    def delete_product(self):
        # Delete user functionality
        pass

