# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175 
# Используя эти данные построить 95% доверительный интервал для 
# разности среднего роста родителей и детей.

import numpy as np
import scipy.stats as stats

# Заданные данные
children_heights = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers_heights = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
confidence_level = 0.95

# Вычисляем средние значения роста детей и родителей
children_mean = np.mean(children_heights)
mothers_mean = np.mean(mothers_heights)

# Вычисляем стандартные отклонения роста детей и родителей
children_std = np.std(children_heights, ddof=1)
mothers_std = np.std(mothers_heights, ddof=1)

# Вычисляем стандартную ошибку разности средних
standard_error = np.sqrt((children_std ** 2) / len(children_heights) + (mothers_std ** 2) / len(mothers_heights))

# Вычисляем критическое значение t-статистики
t_critical = stats.t.ppf((1 + confidence_level) / 2, len(children_heights) + len(mothers_heights) - 2)

# Вычисляем границы доверительного интервала
lower_bound = (children_mean - mothers_mean) - t_critical * standard_error
upper_bound = (children_mean - mothers_mean) + t_critical * standard_error

# Вывод результатов
print("Доверительный интервал:", (lower_bound, upper_bound))