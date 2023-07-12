# 3.Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге
# одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

import numpy as np

# Задаем входные данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])  # Заработная плата
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])  # Целевая переменная

# Добавляем столбец из единиц к данным заработной платы
X = np.column_stack((np.ones(len(zp)), zp))

# Инициализируем начальные значения коэффициентов
alpha = 0.0001
theta = np.zeros(X.shape[1])

# Определяем функцию стоимости (среднеквадратичная ошибка)
def cost_function(theta, X, ks):
    predictions = np.dot(X, theta)
    error = predictions - ks
    cost = np.sum(error**2) / (2 * len(X))
    return cost

# Определяем функцию градиентного спуска
def gradient_descent(theta, X, ks, alpha, iterations):
    costs = []
    for i in range(iterations):
        predictions = np.dot(X, theta)
        error = predictions - ks
        gradient = np.dot(X.T, error) / len(X)
        theta -= alpha * gradient
        cost = cost_function(theta, X, ks)
        costs.append(cost)
    return theta, costs

# Запускаем градиентный спуск
iterations = 1000
theta, costs = gradient_descent(theta, X, ks, alpha, iterations)
print("Коэффициенты линейной регрессии при заработной плате (с intercept):", theta)