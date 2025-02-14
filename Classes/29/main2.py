import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)  # Первый набор данных
y = np.random.rand(100)  # Второй набор данных

# Построение диаграммы рассеяния
plt.scatter(x, y, alpha=0.7, edgecolors='black')
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()