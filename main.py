import random
import time

class Car:
    def __init__(self, make, model, max_speed, fuel_capacity):
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.fuel = fuel_capacity
        self.engine_running = False
        self.distance_covered = 0
        self.is_running = True

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"{self.make} {self.model}: Двигатель запущен.")
        else:
            print(f"{self.make} {self.model}: Двигатель уже работает.")

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print(f"{self.make} {self.model}: Двигатель остановлен.")
        else:
            print(f"{self.make} {self.model}: Двигатель уже остановлен.")

    def drive(self):
        if not self.engine_running:
            print(f"{self.make} {self.model}: Не может ехать, двигатель не запущен.")
            return
        if self.fuel <= 0:
            print(f"{self.make} {self.model}: Нет топлива для движения!")
            self.stop_engine()
            self.is_running = False
            return
        speed = random.randint(0, self.max_speed)
        distance = speed * 0.1
        self.distance_covered += distance
        self.fuel -= distance * 0.1
        print(f"{self.make} {self.model}: Мчится на скорости {speed} км/ч, покрыто {distance:.2f} км.")
        time.sleep(0.1)
        if self.fuel <= 0:
            print(f"{self.make} {self.model}: Топливо закончилось!")
            self.stop_engine()
            self.is_running = False

    def refuel(self, amount):
        if self.fuel + amount > self.fuel_capacity:
            self.fuel = self.fuel_capacity
        else:
            self.fuel += amount
        print(f"{self.make} {self.model}: Заправлено {amount} литров топлива. Текущее топливо: {self.fuel} литров.")

    def status(self):
        return f"{self.make} {self.model}: {self.fuel} литров топлива, {self.distance_covered:.2f} км пройдено."

class Race:
    def __init__(self, name, cars, race_distance):
        self.name = name
        self.cars = cars
        self.race_distance = race_distance
        self.race_over = False

    def start_race(self):
        print(f"Гонка {self.name} началась! Дистанция: {self.race_distance} км.")
        for car in self.cars:
            car.start_engine()

        while not self.race_over:
            self.race_step()

    def race_step(self):
        for car in self.cars:
            if car.is_running:
                car.drive()
                if car.distance_covered >= self.race_distance:
                    print(f"{car.make} {car.model} победил! Дистанция преодолена: {car.distance_covered:.2f} км.")
                    self.race_over = True
                    break

    def show_results(self):
        print("\nРезультаты гонки:")
        for car in self.cars:
            print(car.status())

if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 180, 50)
    car2 = Car("Ford", "Mustang", 200, 60)
    car3 = Car("BMW", "M3", 240, 55)

    race = Race("Speed Championship", [car1, car2, car3], 500)

    race.start_race()
    race.show_results()
