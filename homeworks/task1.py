"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    row_dimension = 0
    col_dimension = 0

    def __init__(self, list2d):
        self.row_dimension = len(list2d[0])
        for row in list2d:
            if len(row) != self.row_dimension:
                raise TypeError("допустимы только квадратные или прямоугольные матрицы")
            for el in row:
                if not (isinstance(el, int) or isinstance(el, float)):
                    raise TypeError("допустимы только числовые значения")
            self.col_dimension += 1
        self.matrix = list2d

    def __str__(self):
        result = ''
        for row in self.matrix:
            line = ' '.join(map(str, row)) + '\n'
            result += line
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Допустимо только сложение матриц")
        if (self.row_dimension != other.row_dimension) or (self.col_dimension != other.col_dimension):
            raise TypeError("допустимо сложение матриц только одинаковой размерности")
        result = []
        for i in range(self.col_dimension):
            tmp_list = []
            for j in range(self.row_dimension):
                tmp_list.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(tmp_list)
        return Matrix(result)


if __name__ == '__main__':
    M1 = Matrix([[1, 2], [3, 4]])
    M2 = Matrix([[1.1, 2], [3, 4]])
    assert str(M1 + M2) == str(Matrix([[2.1, 4], [6, 8]]))
    print(M1)
    print(M2)
    print(M1 + M2)
