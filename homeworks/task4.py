"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
class Car:
    speed = 0

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f"{self.name} поехала")
    def stop(self):
        print(f"{self.name} остановилась")
    def turn(self, direction):
        """
        Поворот налево(left) или направо(right)
        :param 'left' or 'right': type: str
        :return:
        """
        if direction == 'left':
            print(f"{self.name} повернула налево")
        elif direction == 'right':
            print(f"{self.name} повернула направо")
        else:
            print("Направление не определено")
    def show_speed(self):
        print("Текущая скорость", self.speed)

class TownCar(Car):
    def __init__(self, color):
        super().__init__(color, "городская машина", False)
    def show_speed(self):
        if self.speed > 60:
            print("Превышена скорость городской машины:", self.speed)
        else:
            print("Текущая скорость городской машины:", self.speed)

class WorkCar(Car):
    def __init__(self, color):
        super().__init__(color, "Рабочая машина", False)
    def show_speed(self):
        if self.speed > 40:
            print("Превышена скорость Рабочей машины:", self.speed)
        else:
            print("Текущая скорость Рабочей машины:", self.speed)

class SportCar(Car):
    def __init__(self, color):
        super().__init__(color, "Спортивная машина", False)

class PoliceCar(Car):
    def __init__(self):
        super().__init__("Белый", "Полицейская машина", True)

daewoo_matiz = TownCar("Красный")
Kamaz = WorkCar("Оранжевый")
Nissan_350Z = SportCar("Синий")
lada_2114_police = PoliceCar()

car_list = [daewoo_matiz, Kamaz, Nissan_350Z, lada_2114_police]
for car in car_list:
    car.go()
    car.speed = 30
    car.show_speed()
    car.speed = 50
    car.show_speed()
    car.speed = 70
    car.show_speed()
    car.turn('left')
    car.turn('right')
    car.stop()
    print("Это полицейская машина:", car.is_police)
    print("Цвет машины:", car.color)
    print('')

