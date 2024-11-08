class Car:
    def __init__(self, make, model, year, color):
        # Ініціалізація атрибутів автомобіля
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_running = False  # Статус двигуна (не запущений за замовчуванням)

    def start_engine(self):
        # Метод для запуску двигуна
        if not self.engine_running:
            self.engine_running = True
            print(f"Двигун автомобіля {self.make} {self.model} запущено.")
        else:
            print("Двигун вже працює.")

    def stop_engine(self):
        # Метод для зупинки двигуна
        if self.engine_running:
            self.engine_running = False
            print(f"Двигун автомобіля {self.make} {self.model} зупинено.")
        else:
            print("Двигун вже зупинено.")

    def car_info(self):
        # Метод для перегляду інформації про автомобіль
        status = "запущений" if self.engine_running else "зупинений"
        print(f"{self.year} {self.make} {self.model} ({self.color}), двигун {status}.")

# Приклад використання класу
my_car = Car("Toyota", "Corolla", 2020, "синій")
my_car.car_info()  # Виводить інформацію про автомобіль
my_car.start_engine()  # Запускає двигун
my_car.car_info()  # Виводить оновлену інформацію про автомобіль
my_car.stop_engine()  # Зупиняє двигун