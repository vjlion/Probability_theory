# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. 
# Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from scipy.stats import norm

# Ваши данные
X = 174.2
sigma = 5
n = 27
confidence = 0.95

# Критическое значение z
z_critical = norm.ppf((1 + confidence) / 2)

# Доверительный интервал
lower_bound = X - z_critical * (sigma / np.sqrt(n))
upper_bound = X + z_critical * (sigma / np.sqrt(n))

print('Доверительный интервал:', (lower_bound, upper_bound))