from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import QSize

# Clase que representa una ventana con un texto y un botón para regresar al menú principal


class Ventana(QWidget):
    def __init__(self, texto, menu_principal):
        super().__init__()
        self.setWindowTitle(texto)  # Establece el título de la ventana

        # Configura el diseño vertical
        layout = QVBoxLayout()

        # Crea una etiqueta con el texto recibido
        label = QLabel(texto)
        layout.addWidget(label)  # Añade la etiqueta al diseño

        # Crea un botón para regresar al menú principal
        boton_regresar = QPushButton("Regresar al menú principal")
        # Conecta el clic del botón con la función para mostrar el menú principal
        boton_regresar.clicked.connect(menu_principal)
        layout.addWidget(boton_regresar)  # Añade el botón al diseño

        self.setLayout(layout)  # Establece el diseño para la ventana

# Clase que representa el menú principal con 4 botones


class MenuPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        # Establece el título de la ventana
        self.setWindowTitle("Menú Principal")

        # Configura el diseño vertical
        layout = QVBoxLayout()

        # Lista de tuplas con el texto del botón y la función a llamar
        botones = [
            ("Ventana 1", self.abrir_ventana1),
            ("Ventana 2", self.abrir_ventana2),
            ("Ventana 3", self.abrir_ventana3),
            ("Ventana 4", self.abrir_ventana4)
        ]

        # Crea y añade los botones al diseño
        for texto, funcion in botones:
            # Crea un botón con el texto correspondiente
            boton = QPushButton(texto)
            # Conecta el clic del botón con la función correspondiente
            boton.clicked.connect(funcion)
            layout.addWidget(boton)  # Añade el botón al diseño

        self.setLayout(layout)  # Establece el diseño para la ventana

    # Método genérico para abrir una ventana con el texto específico
    def abrir_ventana(self, texto):
        # Crea una instancia de Ventana
        self.ventana = Ventana(texto, self.mostrar_menu)
        self.ventana.resize(300, 200)  # Establece el tamaño de la ventana
        self.ventana.show()  # Muestra la ventana
        self.hide()  # Oculta el menú principal

    # Métodos específicos para abrir cada una de las cuatro ventanas
    def abrir_ventana1(self):
        self.abrir_ventana("Ventana 1")

    def abrir_ventana2(self):
        self.abrir_ventana("Ventana 2")

    def abrir_ventana3(self):
        self.abrir_ventana("Ventana 3")

    def abrir_ventana4(self):
        self.abrir_ventana("Ventana 4")

    # Método para mostrar el menú principal y cerrar la ventana actual
    def mostrar_menu(self):
        self.show()  # Muestra el menú principal
        self.ventana.close()  # Cierra la ventana actual


# Inicialización de la aplicación
app = QApplication([])
menu_principal = MenuPrincipal()  # Crea una instancia del menú principal
menu_principal.resize(300, 200)  # Establece el tamaño del menú principal
menu_principal.show()  # Muestra el menú principal
app.exec()  # Ejecuta el bucle principal de la aplicación
