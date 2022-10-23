#Вариант 12. Грачева Дарья, ИСТбд-22.

#Вычислить сумму знакопеременного ряда, где х - матрица размерности к (квадратная матрица), n - номер слагаемого.
#Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
#У алгоритма д.б. линейная сложность.
#Операция умножения - поэлементная.



import random
import numpy as np
from numpy import linalg


print("Результат работы программы:")

k = int(input("Введите количество строк (столбцов) квадратной матрицы больше 1 и меньше 31: "))
while (k < 1) or (k > 31):
    k = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы больше 1 и меньше 31:"))

x = np.random.randint(5, size=(k,k))
print("Матрица:\n", x)

r = np.linalg.matrix_rank(x)
print("\nРанг матрицы:", r)

accuracy = int(input('Введите минимальное количество знаков после запятой в результате вычисления:'))   #accuracy-точность
accuracy1 = 0.1 ** accuracy

n = 1 #номер слагаемого
factorial = 1
summa = 0
fg = 0
fraction = 1 #fraction-дробь
while abs(fraction) > accuracy1:
    fg += summa
    summa += (-(np.linalg.det(linalg.matrix_power(x, 2 * n - 1)))) / factorial
    n += 1
    factorial = factorial * (2*n - 1) * (2*n - 2)
    fraction = abs(fg-summa)  # считаем разницу
    fg = 0
    print(n - 1, ':', summa, '   ', fraction)
print('\nСумма знакопеременного ряда:', summa)
