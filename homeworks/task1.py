"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time

class TrafficLight:
    __color = {'red': 7, 'yellow': 3, 'green': 2}

    def running(self):
        correct_order = ['red', 'yellow', 'green']
        order = True
        while order:
            for x, (light, wait_time) in enumerate(self.__color.items()):
                if light == correct_order[x]:
                    print(light)
                    time.sleep(wait_time)
                else:
                    print("Нарушен порядок режимов")
                    order = False
                    break


MyTrafficLight = TrafficLight()
MyTrafficLight.running()
