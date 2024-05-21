import sys
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

# Importamos las ventanas
from user_managment_window import UserManagement
from client_managment_window import ClientManagment
from product_managment_window import ProductManagment
from sales_managment_window import SalesManagment
from reporting_window import Reporting


# Función para hacer la database
def init_db():
    conn = sqlite3.connect('erp_sales.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL,
                        name TEXT NOT NULL,
                        lastname TEXT NOT NULL,
                        date_joined DATE NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        RFC TEXT NOT NULL,
                        fiscal_regimen_id INTEGER NOT NULL,
                        address TEXT NOT NULL,
                        city TEXT NOT NULL,
                        state TEXT NOT NULL,
                        zip_code TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS FiscalRegimen (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        code INTEGER NOT NULL,
                        name TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        UPC TEXT NOT NULL,
                        name TEXT NOT NULL,
                        id_presentation INTEGER NOT NULL,
                        price REAL NOT NULL,
                        cost REAL NOT NULL,
                        has_iva BOOLEAN NOT NULL,
                        stock INTEGER NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Presentation (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date_of_sale DATETIME NOT NULL,
                        user_id INTEGER NOT NULL,
                        client_id INTEGER NOT NULL,
                        total_amount REAL NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS ProductSold (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_sale INTEGER NOT NULL,
                        id_product INTEGER NOT NULL,
                        quantity INTEGER NOT NULL,
                        sale_price_per_unit REAL NOT NULL)''')
    
    # Insert default admin user
    cursor.execute('''INSERT OR IGNORE INTO Users (username, password, role, name, lastname, date_joined) 
                      VALUES ('admin', 'admin', 'Admin', 'Default', 'Admin', DATE('now'))''')
    
    conn.commit()
    conn.close()

# Hacemos las clases de user, cliente, etc.

class User:
    def __init__(self, username, password, role, name, lastname):
        self.id = None
        self.username = username
        self.password = password
        self.role = role
        self.name = name
        self.lastname = lastname
        self.date_joined = datetime.now().date()

class Client:
    def __init__(self, name, RFC, fiscal_regimen_id, address, city, state, zip_code):
        self.id = None
        self.name = name
        self.RFC = RFC
        self.fiscal_regimen_id = fiscal_regimen_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

class FiscalRegimen:
    def __init__(self, code, name):
        self.id = None
        self.code = code
        self.name = name

class Product:
    def __init__(self, UPC, name, id_presentation, price, cost, has_iva, stock):
        self.id = None
        self.UPC = UPC
        self.name = name
        self.id_presentation = id_presentation
        self.price = price
        self.cost = cost
        self.has_iva = has_iva
        self.stock = stock

class Presentation:
    def __init__(self, name):
        self.id = None
        self.name = name

class Sale:
    def __init__(self, user_id, client_id, total_amount):
        self.id = None
        self.date_of_sale = datetime.now()
        self.user_id = user_id
        self.client_id = client_id
        self.total_amount = total_amount

class ProductSold:
    def __init__(self, id_sale, id_product, quantity, sale_price_per_unit):
        self.id = None
        self.id_sale = id_sale
        self.id_product = id_product
        self.quantity = quantity
        self.sale_price_per_unit = sale_price_per_unit


# Ventana principal del login
class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        username_label = QLabel(self)
        username_label.setText("Username: ")
        username_label.setFont(QFont("Arial", 10))

        self.username_input = QLineEdit(self)
        self.username_input.resize(250, 24)
        self.username_input.setStyleSheet("background-color: #FFFFFF;")
        
        password_label = QLabel(self)
        password_label.setText("Password: ")
        password_label.setFont(QFont("Arial", 10))

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.setStyleSheet("background-color: #FFFFFF;")
        
        
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.check_credentials)
        
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)
        self.setWindowTitle('ERP Sales System - Login')
        self.show()

    # Función para checar las credenciales de quien va a hacer login
    def check_credentials(self):

        # Metemos como input los datos del usuario
        username = self.username_input.text()
        password = self.password_input.text()

        # Nos conectamos a la data base
        conn = sqlite3.connect('erp_sales.db')
        cursor = conn.cursor()
        
        # Buscamos en la database, si existe nos devuelve el usuario
        cursor.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        
        # Si es verdadero, hacemos login
        if user:
            QMessageBox.information(self, 'Success', 'Login Successful')
            self.main_window = MainWindowAdmin()
            self.main_window.show()
            self.close()
        # Si no es verdadero, nos manda error y volvemos a la pagina principal
        else:
            QMessageBox.warning(self, 'Error', 'Invalid Credentials')

        # Cerramos la conexión
        conn.close()


# Esta ventana se enseña después de hacer el login correctamente con el usuario admin
class MainWindowAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Principal")
        layout = QVBoxLayout()

        # Crear y añadir los botones al diseño
        botones = [
            ("User Managment", self.user_managment),
            ("Client Management", self.client_managment),
            ("Product Management", self.product_managment),
            ("Sales Management", self.sales_managment),
            ("Reporting", self.reporting),
            ("Log Out", self.logout)
            
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)


        self.setLayout(layout)
        self.show()

    # Ver como sacar las funciones para que dependiendo del rol las podamos usar 
    # En vez de copiar y pear
    def user_managment(self):
        self.ventana = UserManagement(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def client_managment(self):
        self.ventana = ClientManagment(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def product_managment(self):
        self.ventana = ProductManagment(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def sales_managment(self):
        self.ventana = SalesManagment(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def reporting(self):
        self.ventana = Reporting(self.mostrar_menu)
        self.ventana.show()
        self.hide()

    def logout(self):
        self.close()

    def mostrar_menu(self):
        self.show()
        self.ventana.close()



#! You can create similar classes for `ClientManagement`, `ProductManagement`, and `SalesManagement`.

### Running the Application

if __name__ == '__main__':

    init_db()
    app = QApplication(sys.argv)
    login = LoginForm()
    sys.exit(app.exec())
