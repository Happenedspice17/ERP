from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from user_managment_window import Ventana1
from sales_managment_window import Ventana2
from ventana_1 import Ventana3
from ventana_4 import Ventana4


class MenuPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Principal")
        layout = QVBoxLayout()

        # Crear y añadir los botones al diseño
        botones = [
            ("Ventana 1", self.abrir_ventana1),
            ("Ventana 2", self.abrir_ventana2),
            ("Ventana 3", self.abrir_ventana3),
            ("Ventana 4", self.abrir_ventana4)
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        self.setLayout(layout)

    def abrir_ventana1(self):
        self.ventana = Ventana1(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def abrir_ventana2(self):
        self.ventana = Ventana2(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def abrir_ventana3(self):
        self.ventana = Ventana3(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def abrir_ventana4(self):
        self.ventana = Ventana4(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def mostrar_menu(self):
        self.show()
        self.ventana.close()


app = QApplication([])
menu_principal = MenuPrincipal()
menu_principal.resize(300, 200)
menu_principal.show()
app.exec()
