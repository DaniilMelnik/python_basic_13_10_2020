"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):  # день-месяц-год
        self.text_date = date

    @classmethod
    def to_num(cls, Date):
        tmp_list = Date.text_date.split('-')
        if not all(list(map(lambda x: x.isdigit(), tmp_list))):
            raise TypeError("Неверный формат даты")
        try:
            day, month, year = map(int, tmp_list)
        except:
            raise TypeError("Допустим формат даты только в виде целого числа")
        else:
            return day, month, year

    @staticmethod
    def check(day, month, year):
        if not day in range(0, 32):
            return False
        if not month in range(0, 13):
            return False
        if (year < 0) or (year > 10000):
            print("Проверьте величину года")
        return True


if __name__ == '__main__':
    assert Date.to_num(Date("05-08-2005")) == (5, 8, 2005)
    assert Date.check(*Date.to_num(Date("03-12-2013")))
    assert not Date.check(*Date.to_num(Date("32-12-2013")))
    assert not Date.check(*Date.to_num(Date("13-13-2013")))
