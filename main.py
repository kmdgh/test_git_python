class Car:
    def __init__(self, name, volume, max_speed, acceleration):
        self.name = name
        self.volume = volume
        self.max_speed = max_speed
        self.acceleration = acceleration

    def get_info(self):
        return f"Name: {self.name}\nVolume: {self.volume} liters\nMax speed: {self.max_speed} km/h\nAcceleration: {self.acceleration} s\n\n"


lamborghini_countach = Car('Lamborghini Countach', 8, 300, 2.2)
nissan_GTR = Car('Nissan GTR', 8, 300, 2.2)
honda_civic = Car('Honda Civic', 8, 300, 2.2)
porsche_911_gt3_RS = Car('Porsche 911 GT3 RS', 8, 300, 2.2)
cars_arr = [lamborghini_countach, nissan_GTR, honda_civic, porsche_911_gt3_RS]
# car = input("Введите название машины из списка для большей информации")

for car in cars_arr:
    print(car.get_info())
