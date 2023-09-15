import random


class DescrRnd:
    n = 0
    x = []
    p = []
    f = []

    # конструктор

    def __init__(self):
        self.n = 4
        self.x = [f'x{i+1}' for i in range(self.n)]
        self.p = [0.20, 0.30, 0.45, 0.05]
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


if __name__ == '__main__':

    dRnd = DescrRnd()

    n = int(input("Введите число генерируемых значений: "))
    print('последовательность значений:')
    for i in range(n):
        print(dRnd.GenValue(), end="")

    print(f"\n{dRnd.GetFreqs()}")
