# Известно, что генеральная совокупность распределена нормально 
# со средним квадратическим отклонением, равным 16. Найти доверительный 
# интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.

import scipy.stats as stats

# Заданные значения
sigma = 16
M = 80
n = 256
confidence_level = 0.95

# Вычисляем стандартную ошибку
standard_error = sigma / (n ** 0.5)

# Вычисляем критическое значение t-статистики
t_critical = stats.t.ppf((1 + confidence_level) / 2, n - 1)

# Вычисляем границы доверительного интервала
lower_bound = M - t_critical * standard_error
upper_bound = M + t_critical * standard_error

# Вывод результатов
print("Доверительный интервал:", (lower_bound, upper_bound))