import sys
import sqlite3
from classes import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

# 1. **Database setup**
# 2. **Data models (classes)**
# 3. **GUI setup using PyQt**
# 4. **Core functionalities implementation**

# 1. Database Setup

# First, we'll create an SQLite database and set up the tables for users, clients, products, sales, and other entities.


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


### 3. GUI Setup using PyQt

# We'll use PyQt to create the graphical user interface.


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

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect('erp_sales.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        
        if user:
            QMessageBox.information(self, 'Success', 'Login Successful')
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Invalid Credentials')

        conn.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ERP Sales System')
        self.setGeometry(100, 100, 800, 600)
        
        # Add main window components here
        
        self.show()

### 4. Core Functionalities Implementation

#Next, we’ll add the core functionalities like user management, client management, product management, and sales management. Here’s an example for user management:

class UserManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.add_user_button = QPushButton('Add User', self)
        self.add_user_button.clicked.connect(self.add_user)
        
        self.edit_user_button = QPushButton('Edit User', self)
        self.edit_user_button.clicked.connect(self.edit_user)
        
        self.view_users_button = QPushButton('View Users', self)
        self.view_users_button.clicked.connect(self.view_users)
        
        self.delete_user_button = QPushButton('Delete User', self)
        self.delete_user_button.clicked.connect(self.delete_user)
        
        layout.addWidget(self.add_user_button)
        layout.addWidget(self.edit_user_button)
        layout.addWidget(self.view_users_button)
        layout.addWidget(self.delete_user_button)
        
        self.setLayout(layout)
        self.setWindowTitle('User Management')
        self.show()

    def add_user(self):
        # Add user functionality
        pass

    def edit_user(self):
        # Edit user functionality
        pass

    def view_users(self):
        # View users functionality
        pass

    def delete_user(self):
        # Delete user functionality
        pass

#! You can create similar classes for `ClientManagement`, `ProductManagement`, and `SalesManagement`.

### Running the Application

if __name__ == '__main__':

    init_db()
    app = QApplication(sys.argv)
    login = LoginForm()
    sys.exit(app.exec())
