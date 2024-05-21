from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel


class Ventana3(QWidget):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Ventana 3")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ventana 3"))
        boton_regresar = QPushButton("Regresar al menú principal")
        boton_regresar.clicked.connect(menu_principal)
        layout.addWidget(boton_regresar)
        self.setLayout(layout)
