from datetime import datetime

class Product:
    def __init__(self, name, price, manufacturer):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer

class Market(Product):
    def __init__(self, name, price, manufacturer, date_create, product_sale):
        super().__init__(name, price, manufacturer)
        self.date_create = date_create
        self.product_sale = product_sale

    def apply_discount(self):
        current_year = datetime.now().year
        product_year = self.date_create.year

        if current_year - product_year > 2:
            discount = (self.price * self.product_sale) / 100
            self.price -= discount

    def display_info(self):
        print(f"Tovar nomi: {self.name}")
        print(f"Tovar narxi: {self.price:.2f} so'm")
        print(f"Tovar ishlab chiqaruvchi: {self.manufacturer}")
        print(f"Tovar yaratilgan sana: {self.date_create}")
        print(f"Tovarga qo'yilgan skidka: {self.product_sale}%")

product = Market(
    name=input("Tovar nomini kiriting: "),
    price=float(input("Tovar narxini kiriting (so'mda): ")),
    manufacturer=input("Tovar ishlab chiqaruvchini kiriting: "),
    date_create=datetime.strptime(input("Tovar yaratilgan sanasini kiriting (yyyy-mm-dd): "), '%Y-%m-%d'),
    product_sale=float(input("Tovarga qo'yilgan skidkani kiriting (%da): "))
)

product.apply_discount()

product.display_info()
