"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
from collections import defaultdict


def isequipment(func):
    def wrapper(self, *args):
        for arg in args:
            if not isinstance(arg, Equipment):
                raise TypeError("аргумент не является оргтехникой")
            return func(self, *args)
    return wrapper


class Storage:
    def __init__(self, name):
        self.box = defaultdict(int)
        self.name = name

    @isequipment
    def add_equipment(self, eq):
        self.box[eq] += 1

    @isequipment
    def del_equipment(self, eq):
        self.box[eq] -= 1
        if self.box[eq] == 0:
            self.box.pop(eq)

    def send(self, other, eq, number):
        if all([isinstance(other, Storage), isinstance(eq, Equipment), isinstance(number, int)]):
            for _ in range(number):
                self.del_equipment(eq)
                other.add_equipment(eq)
        else:
            raise TypeError("Ошибка ввода данных")

    def show_equipment(self):
        print(f"Товары на складе {self.name}: ")
        for key, val in self.box.items():
            print(f"{key.name} : {val}")
        print("")

    def show_data(self):
        for key in self.box:
            print(key)


class Equipment:
    def __init__(self, name, type, country):
        self.name = name
        self.type = type
        self.country = country

    def __str__(self):
        return f"name = {self.name}, country = {self.country}"


class Printer(Equipment):
    def __init__(self, name, country, print_technology, n_colors):
        self.print_technology = print_technology
        self.n_colors = n_colors
        super().__init__(name, "printer", country)

    def __str__(self):
        return super().__str__() + f", print_technology = {self.print_technology}, n_colors = {self.n_colors}"


class Scaner(Equipment):
    def __init__(self, name, country, resolution):
        self.resolution = resolution
        super().__init__(name, "scaner", country)

    def __str__(self):
        return super().__str__() + f", resolution = {self.resolution}"


class Xerox(Equipment):
    def __init__(self, name, country, print_speed):
        self.print_speed = print_speed
        super().__init__(name, "Xerox", country)

    def __str__(self):
        return super().__str__() + f", print_speed = {self.print_speed}"


if __name__ == '__main__':
    # Инициализация хранилищ
    storageA = Storage("old_land")
    storageB = Storage("new_land")
    # Создание техники
    canon = Printer('canon', 'Thailand', 'spray', 256)
    epson = Scaner('epson', 'Indonesy', 4800)
    HP = Xerox('HP', ' china', 18)
    # Заполнение склада А
    eq_list = [canon, epson, HP, canon, canon, HP]
    for el in eq_list:
        storageA.add_equipment(el)
    storageA.show_equipment()
    # Передача canon на склад 3
    storageA.send(storageB, canon, 3)
    storageA.show_equipment()
    storageB.show_equipment()
    # Данные о товарах на складе B
    storageB.show_data()


