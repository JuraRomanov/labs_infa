import random
import math


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
    e = 2.71828182845905
    xMin, xMax = -1, 1
    n = 0
    f = []
    dx = 0

    def __init__(self, xMin=-5, xMax=5, n=10):
        self.xMin, self.xMax = xMin, xMax
        self.n = n
        self.f = [0]*self.n
        self.dx = int((self.xMax - self.xMin) / self.n)

    # индексатор по массиву частот
    def GetValueFromArr(self, index):

        return self.f[index] if index >= 0 and index < self.n else self.f[0]

    def GeneralLogNormalValue(self, _b, _c):
        t = 0.0
        m = 12
        for i in range(m):
            t += random.random()
        t -= m/2

        x  = pow(self.e, _c*t+ _b)
        self.CountFreqs(x)
        return x

    def CountFreqs(self, _x):
        # print(_x)
        for i in range(self.n):
            # print(f'i={i} vor ={_x>self.xMin + i*self.dx} and {self.xMin + (i+1) * self.dx}')
            if ((_x > self.xMin + i*self.dx) and (_x < self.xMax + (i+1) * self.dx)):
                
                
                self.f[i] += 1
                # print(f'_x = {_x} i={i} f={self.f[i]}')
                break


if __name__ == '__main__':

    # dRnd = ConrinRnd()

    # n = int(input("Введите число генерируемых значений: "))
    # print('последовательность значений:')
    # for i in range(n):
    #     print(dRnd.GenValue(), end="")

    # print(f"\n{dRnd.GetFreqs()}")
    print(math.e)
    xMin = -24
    xMax = 2
    n = 15
    cRnd = ConrinRnd(xMin, xMax, n)
    m = int(input("Введите число генерируемых значений:\n"))

    b = 1
    c = 0.5
    buf = ""

    for i in range(m):
        buf += f'{i}. {cRnd.GeneralLogNormalValue(b,c)}\n'

    print(f'Последовательность значений:\n{buf}')
    f = []
    # for i in range(n):
    #     f.append(cRnd.f[i])
    #     print(f'Интервал {i}: {f[i]}')
    print(cRnd.f)
    # DrawGistogram(f)
