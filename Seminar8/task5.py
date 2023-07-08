# Измерены значения IQ выборки студентов, обучающихся в местных технических вузах: 
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111. 
# Известно, что в генеральной совокупности IQ распределен нормально. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from scipy.stats import t

# Ваши данные
data = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
n = len(data)
confidence = 0.95

# Среднее значение выборки
mean = np.mean(data)

# Стандартное отклонение выборки
std = np.std(data, ddof=1)

# Стандартная ошибка среднего
SE = std / np.sqrt(n)

# Критическое значение t
t_critical = t.ppf(q=(1 + confidence) / 2, df=n - 1)

# Доверительный интервал
lower_bound = mean - t_critical * SE
upper_bound = mean + t_critical * SE

print('Доверительный интервал:', (lower_bound, upper_bound))