import sys
import sqlite3
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtGsui import QPalette, QColor


class login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
        self.init_db()

    def inicializar_ui(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle("Mi login")
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#E0E0E0"))
        self.setPalette(palette)
        self.generar_formulario()
        self.show()

    def init_db(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.c = self.conn.cursor()
        self.c.execute('''
           CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE,
               password TEXT
           )
       ''')
        self.conn.commit()

    def agregar_usuario(self):
        username = self.user_input.text()
        password = self.password_input.text()
        try:
            self.c.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.conn.commit()
            QMessageBox.information(
                self, 'Éxito', 'Usuario añadido exitosamente!')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'El usuario ya existe.')

    def eliminar_usuario(self):
        username = self.user_input.text()
        self.c.execute('DELETE FROM users WHERE username = ?', (username,))
        self.conn.commit()
        QMessageBox.information(self, 'Éxito', 'Usuario eliminado.')

    def mostrar_usuario(self):
        username = self.user_input.text()
        self.c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = self.c.fetchone()
        if user:
            QMessageBox.information(self, 'Usuario encontrado', f'Usuario: {
                                    user[0]}, Contraseña: {user[1]}')
        else:
            QMessageBox.warning(self, 'No encontrado',
                                'Usuario no encontrado.')

    def mostrar_todos(self):
        self.c.execute('SELECT * FROM users')
        users = self.c.fetchall()
        msg = '\n'.join([f'Usuario: {user[0]}, Contraseña: {
                        user[1]}' for user in users])
        QMessageBox.information(self, 'Todos los usuarios', msg)

    def generar_formulario(self):
        user_label = QLabel(self)
        user_label.setText("usuario: ")
        user_label.setFont(QFont("Arial", 10))
        user_label.move(20, 54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 50)
        self.user_input.setStyleSheet("background-color: #FFFFFF;")

        password_label = QLabel(self)
        password_label.setText("password: ")
        password_label.setFont(QFont("Arial", 10))
        password_label.move(20, 86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.move(90, 82)
        self.password_input.setStyleSheet("background-color: #FFFFFF;")

        self.boton1 = QPushButton("Añadir Usuario", self)
        self.boton1.move(20, 120)
        self.boton1.clicked.connect(self.agregar_usuario)

        self.boton2 = QPushButton("Eliminar Usuario", self)
        self.boton2.move(90, 120)
        self.boton2.clicked.connect(self.eliminar_usuario)

        self.boton3 = QPushButton("Mostrar Usuario", self)
        self.boton3.move(160, 120)
        self.boton3.clicked.connect(self.mostrar_usuario)

        self.boton4 = QPushButton("Mostrar Todos", self)
        self.boton4.move(230, 120)
        self.boton4.clicked.connect(self.mostrar_todos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_login = login()
    sys.exit(app.exec())
