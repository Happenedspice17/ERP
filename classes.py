from datetime import datetime

### 2. Data Models (Classes)

#We create data models to encapsulate the information for users, clients, products, etc.


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