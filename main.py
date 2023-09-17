# библиотеки
import random
import math
import openpyxl
from openpyxl.chart import BarChart, Reference

# классы


class DescrRnd:
    n = 0
    x = []
    p = []
    f = []

    # конструктор

    def __init__(self):
        self.n = 8
        self.x = [f'x{i+1}' for i in range(self.n)]
        self.p = [0.16, 0.08, 0.05, 0.18, 0.11, 0.15, 0.07, 0.2]
        self.f = [0]*self.n

    # генерация случайного значения

    def GenValue(self):
        y = ""  # значения на выходе
        rnd = random.random()  # случайное число
        q = 0.0  # нижняя граница
        for i in range(self.n):
            if (rnd > q and rnd <= q + self.p[i]):
                y = self.x[i]
                self.f[i] += 1
                break
            q += self.p[i]
        return y

    def GetFreqs(self):
        buf = 'частота появления значений:\n'
        for i in range(self.n):
            buf += f"x{i+1} - {self.f[i]}\n"
        return buf


class MakarovChain:
    m = 8  # константа
    s = []  # массив состояний
    p = []  # массив переходных состояний
    f = []  # массив частот
    k = 0  # индекс текущего состояния

    # конструктор
    def __init__(self):

        self.s = [f's{i+1}' for i in range(self.m)]
        self.p = [[0.14, 0.2, 0.02, 0.27, 0.09, 0.02, 0.1, 0.16],
                  [0.2, 0.05, 0.13, 0.08, 0.2, 0.13, 0.2, 0.01],
                  [0.06, 0.2, 0.16, 0.22, 0.12, 0.09, 0.05, 0.1],
                  [0.07, 0.18, 0.2, 0.04, 0.2, 0.09, 0.1, 0.12],
                  [0.09, 0.3, 0.09, 0.2, 0.01, 0.1, 0.07, 0.15],
                  [0.04, 0.1, 0.1, 0.05, 0.28, 0.07, 0.23, 0.13],
                  [0.15, 0.06, 0.07, 0.2, 0.2, 0.08, 0.2, 0.04],
                  [0.2, 0.03, 0.16, 0.1, 0.09, 0.1, 0.07, 0.25]]
        self.f = [0]*self.m
        self.k = random.randint(0, self.m-1)

    def GenerState(self):
        st = ""  # текущее состояние цепи
        x = random.random()
        q = 0.0  # кумулятивная вероятyость

        for i in range(self.m):
            if ((x > q) and (x <= q + self.p[self.k][i])):
                st = self.s[i]
                self.k = i
                self.f[i] += 1
                break
            q += self.p[self.k][i]

        return st

    def GetFreqs(self):
        buf = 'частота появления состояний:\n'
        for i in range(self.m):
            buf += f"s{i+1} - {self.f[i]}\n"
        return buf


class ConrinRnd:
    xMin, xMax = -1, 1
    f = []
    data = []

    # конструктор
    def __init__(self, _xMin=-8, _xMax=1, _numSamples=10):
        self.xMin, self.xMax = _xMin, _xMax
        self.numSamples = _numSamples
        self.f = [0]*self.numSamples

    def GenKoshi(self, _a, _numSamples):
        self.data = []
        buf = ""
        for _ in range(_numSamples):
            u1 = random.random()
            x = self.xMin + (self.xMax - self.xMin) * u1
            u2 = random.random()
            # Функция плотности распределения Коши
            y = _a * (1 / (math.pi * _a * (1 + ((x - _a) / _a) ** 2)))
            if u2 < y:
                self.data.append(x)
            buf += f"{_}: {x}\n"

        return buf

    def CountFreqs(self):
        data = []
        # Фильтрация значений, чтобы они попадали в интервал (xmin, xmax)
        filtered_data = [x for x in self.data if self.xMin <= x <= self.xMax]
        print("Набор значений НСВ с распределением Коши:")
        for index, value in enumerate(filtered_data):
            print(f'{index+1}:{value}')

        # Разбивка интервала (xmin, xmax) на бины и подсчет частот попадания значений
        num_bins = 10
        bin_width = (self.xMax - self.xMin) / num_bins
        hist = [0] * num_bins
        for value in filtered_data:
            bin_index = int((value - self.xMin) / bin_width)
            hist[bin_index] += 1

        # Вывод частот попадания в интервалы
        for i in range(num_bins):
            bin_start = self.xMin + i * bin_width
            bin_end = bin_start + bin_width
            print(f'Интервал №{i} ({bin_start:.2f}, {bin_end:.2f}): {hist[i]}')
            data.append([i, hist[i]])

        return data
# функции


def DrawGistogram(_data):
    # Создаем новую книгу Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    data = [
        ['Категория', 'Значение'],
    ]
    data += _data

    for row in data:
        sheet.append(row)

    # Создаем объект гистограммы
    chart = BarChart()
    chart.type = "col"
    chart.style = 13
    chart.title = "гистограмма распределения значений"
    chart.x_axis.title = "Категории"
    chart.y_axis.title = "Значения"

    # Указываем диапазон данных для гистограммы

    data_range = Reference(sheet, min_col=2, min_row=1,
                           max_col=2, max_row=len(data))
    labels = Reference(sheet, min_col=1, min_row=2, max_row=len(data))

    chart.add_data(data_range, titles_from_data=True)
    chart.set_categories(labels)

    # Вставляем гистограмму в лист Excel
    sheet.add_chart(chart, "E5")

    # сохранияем книгу
    workbook.save("гистограмма.xlsx")


if __name__ == '__main__':

    a = 1.25
    xMin = -8
    xMax = 1

    numSamples = int(input("Введите число генерируемых значений:\n"))
    cRnd = ConrinRnd(xMin, xMax, numSamples)

    loc = 0
    scale = 1  # параметр масштаба
    buf = ""

    print(cRnd.GenKoshi(a, numSamples))
    data = cRnd.CountFreqs()

    DrawGistogram(data)
