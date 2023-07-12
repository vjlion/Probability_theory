# 1.Даны значения величины заработной платы заемщиков банка (zp) и 
# значения их поведенческого кредитного скоринга (ks): 
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
# Используя математические операции, посчитать коэффициенты 
# линейной регрессии, приняв за X заработную плату 
# (то есть, zp - признак), а за y - значения скорингового балла 
# (то есть, ks - целевая переменная). 
# Произвести расчет как с использованием intercept, так и без.


# Для расчета коэффициентов линейной регрессии с использованием intercept, мы будем использовать формулу:
# β = (X^T * X)^(-1) * X^T * y

# где β - вектор коэффициентов регрессии,
# X - матрица признаков (заработная плата),
# y - вектор целевой переменной (скоринговый балл).

import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Расчет с перехватом (intercept)
X_with_intercept = np.column_stack((np.ones(len(zp)), zp))
coefficients_with_intercept = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ ks
a_with_intercept = coefficients_with_intercept[0]  # перехват
b_with_intercept = coefficients_with_intercept[1]  # коэффициент при зп

# Расчет без перехвата (intercept)
X_without_intercept = zp.reshape(-1, 1)
coefficients_without_intercept = np.linalg.inv(X_without_intercept.T @ X_without_intercept) @ X_without_intercept.T @ ks
b_without_intercept = coefficients_without_intercept[0]  # коэффициент при зп

print("Коэффициенты линейной регрессии с перехватом:")
print("a =", a_with_intercept)
print("b =", b_with_intercept)

print("Коэффициент линейной регрессии без перехвата:")
print("b =", b_without_intercept)

