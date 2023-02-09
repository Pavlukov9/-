# Исходная функция:
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1) Определить корни
# 2) Найти интервалы, на которых функция возрастает
# 3) Найти интервалы, на которых функция убывает
# 4) Построить график
# 5) Вычислить вершину
# 6) Определить промежутки, на котором f > 0
# 7) Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
import numpy as np

A = -12
B = -18
C = 5
D = 10
E = -30

# Зададим интервал:
x = np.arange(-100, 100, 0.001)

# Интервал, на котором будем искать корень и вершину:
x_cut = np.arange(79, 83, 0.001)

# Создадим саму функцию:
def func(x):
    function = A*np.sin(np.cos(x))*x**4 + B*x**3 + D*x**2 + C*x + E
    return function

# Ищем корень:
root = 79
for i in np.arange(79, 83, 0.001):
    if np.absolute(func(root)) > np.absolute(func(i)):
        root = i

# Ищем вершину:
min_func = min(func(x))
def extr_func(x, min_func):
    extremum_function = A*np.sin(np.cos(x))*x**4 + B*x**3 + D*x**2 + C*x + E -min_func
    return extremum_function

extr_x_cut = 79
for i in np.arange(79, 83, 0.001):
    if np.absolute(extr_func(extr_x_cut, min_func)) > np.absolute(extr_func(i, min_func)):
        extr_x_cut = i

x_range_down = np.arange(79, extr_x_cut, 0.001)
x_range_up = np.arange(extr_x_cut, 83, 0.001)

# Построение графика:
fig, ax = plt.subplots()
ax.set_title(f"""Рассмотрим участок по оси Х: (79; 83)
Корень функции на этом участке: x = {round(root, 2)}
Вершина функции на этом участке: x = {round(extr_x_cut, 2)}""")
ax.set_xlabel('Ось Х')
ax.set_ylabel('Ось У')
ax.grid()
ax.plot(x,func(x),'y')
ax.plot(x_range_down, func(x_range_down), 'r', label = 'Функция убывает')
ax.plot(x_range_up, func(x_range_up), 'g', label = 'Функция возрастает')
ax.legend()
plt.show()
