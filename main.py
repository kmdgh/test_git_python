class Car:
    def __init__(self, name, volume, max_speed, acceleration):
        self._name = name
        self._volume = volume
        self._max_speed = max_speed
        self._acceleration = acceleration

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = volume

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        self._max_speed = max_speed

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        self._acceleration = acceleration

    def get_info(self):
        return f"Name: {self._name}\nVolume: {self._volume} liters\nMax speed: {self._max_speed} km/h\nAcceleration: {self._acceleration} s\n\n"


lamborghini_countach = Car('Lamborghini Countach', 8, 300, 2.2)
nissan_GTR = Car('Nissan GTR', 8, 300, 2.2)
honda_civic = Car('Honda Civic', 8, 300, 2.2)
porsche_911_gt3_RS = Car('Porsche 911 GT3 RS', 8, 300, 2.2)
cars_arr = [lamborghini_countach, nissan_GTR, honda_civic, porsche_911_gt3_RS]
# car = input("Введите название машины из списка для большей информации")

for car in cars_arr:
    print(car.get_info())

choice = 1
while choice != 0:
    print("Enter 1 to create new car")
    print("Enter 2 to check garage")
    print("Enter 0 to leave")
    choice = int(input())

    if choice == 1:
        name = input("Enter car name")
        volume = input("Enter car volume")
        max_speed = input("Enter car max_speed")
        acceleration = input("Enter car acceleration")
        name = Car(name, volume, max_speed, acceleration)
        cars_arr.append(name)
    elif choice == 2:
        for car in cars_arr:
            print(car.get_info())

#feature branch update