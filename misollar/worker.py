class Worker:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary

    def increase_salary(self):
        self.salary *= 1.15

    def update_position(self):
        if self.surname.startswith('Abdulla'):
            self.position += ' injener'

    def display_info(self):
        print(f"Familyasi: {self.surname}, Lavozimi: {self.position}, Oyligi: {self.salary:.2f} so'm")

# 5 ta obyektdan iborat ro'yxat
workers = [
    Worker('Abdullaev', 'Menejer', 3000000),
    Worker('Karimov', 'Dasturchi', 4500000),
    Worker('Abdullayev', 'Mexanik', 3500000),
    Worker('Rustamov', 'Texnik', 2800000),
    Worker('Ismoilov', 'Buxgalter', 3200000)
]

# Har bir ishchining oyligini 15%ga oshirish va ma'lumotlarni chiqarish
for worker in workers:
    worker.increase_salary()
    worker.update_position()
    worker.display_info()
