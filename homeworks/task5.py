"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    title = 'Stationery'
    def draw(self):
        print("start draw")
class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print(f"{self.title} draw")
class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print(f"{self.title} draw")

class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print(f"{self.title} draw")

Parker = Pen()
koh_i_nor = Pencil()
brauberg = Handle()

Parker.draw()
koh_i_nor.draw()
brauberg.draw()