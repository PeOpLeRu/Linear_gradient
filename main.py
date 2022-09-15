import numpy as np
import matplotlib.pyplot as plt
import time

def lerp(v0, v1, t):    # Функция расчета смешения цветов
    return (1 - t) * v0 + t * v1

size = 10000    # Размер квадрата
image = np.zeros((size, size, 3), dtype="uint8")    # матрица, размером size*size с элементом значения цвета [r, g, b]

assert image.shape[0] == image.shape[1]    # Проверки
assert image.shape[0] == size

color1 = [0, 128, 255]    # Цвета градиента
color2 = [255, 128, 0]

step = 0.5 / size    # Шаг смещения цвета для каждой строки
dynamic_inc = step    # Счетчик, аккумулируюищй смещения

start_time = time.time()
for row in range(size):    # Для каждой строки
    for i in range(size):    # Расчет для каждого пикселя строки его цвета
        temp = (step*(i+1)) + dynamic_inc
        r = lerp(color1[0], color2[0], temp)
        g = lerp(color1[1], color2[1], temp)
        b = lerp(color1[2], color2[2], temp)
        image[row, i, :] = [r, g, b]
    dynamic_inc += step    # Для следующей строки смещаем цвет

print("Время выполнения кода: {time}".format(time=time.time() - start_time))

plt.figure(1)
plt.imshow(image)    # График
plt.show()