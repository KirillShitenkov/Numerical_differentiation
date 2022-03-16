import re
import numpy as np
import matplotlib.pyplot as plt

replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
]

def string_to_funcX(string1):
    for word in re.findall('[a-zA-Z_]+', string1):
        if word not in allowed_words:
            raise ValueError(
                '"{}" запрещен для использования в математических выражениях'.format(word)
            )
    for old, new in replacements.items():
        string1 = string1.replace(old, new)
    def func1(x):
        return eval(string1)
    return func1

def main():
    func1 = string_to_funcX(input("Введите функцию F(x): "))
    a = float(input("Введите начало отрезка a: "))
    b = float(input("Введите конец отрезка b: "))
    h = float(input("Введите размер шага h: "))
    print("1 - Конечная разность вперед.")
    print("2 - Конечная разность назад.")
    print("3 - Симметричная конечная разность.")
    method = int(input("Выберите метод вычисдения производной: "))
    f = []
    X = []
    F = []
    X.append(a)
    if method == 1: 
        while X[-1] <= b:
            f_cur = (func1(X[-1] + h) - func1(X[-1])) / h
            f.append(f_cur)
            X.append(X[-1] + h)
    if method == 2:
        while X[-1] <= b:
            f_cur = (func1(X[-1]) - func1(X[-1] - h)) / h
            f.append(f_cur)
            X.append(X[-1] + h)
    if method == 3:
        while X[-1] <= b:
            f_cur = (func1(X[-1] + h) - func1(X[-1] - h)) / h
            f.append(f_cur)
            X.append(X[-1] + h)
    X.pop()
    for i in range(len(X)): 
        F.append(func1(X[i]))
    plt.figure("Diff")
    plt.plot(X, f, label = "F'(x)")
    plt.plot(X, F, label = "F(x)")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()