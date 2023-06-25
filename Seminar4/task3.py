# Непрерывная случайная величина X распределена нормально и 
# задана плотностью распределения f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)

# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)

import scipy.stats as stats
import math

mu = -2
sigma = 4

# M(X)
mean = mu
print("Математическое ожидание:", mean)

# D(X)
variance = sigma ** 2
print("Дисперсия:", variance)

# std(X)
std_dev = sigma
print("Cреднее квадратичное отклонение:", std_dev)
 

# Ответ: 
# а). M(X) = -2
# б). D(X) = 16
# в). std(X) = 4