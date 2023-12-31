# Провести дисперсионный анализ для определения того, 
# есть ли различия среднего роста среди взрослых футболистов, 
# хоккеистов и штангистов. Даны значения роста в трех группах 
# случайно выбранных спортсменов: 
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. 
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170

# Для проведения дисперсионного анализа необходимо выполнить следующие шаги:
# 1. Сформулировать нулевую и альтернативную гипотезы:
# - Нулевая гипотеза (H0): средний рост футболистов, хоккеистов и штангистов одинаковый.
# - Альтернативная гипотеза (H1): средний рост футболистов, хоккеистов и штангистов различается.

# 2. Вычислить средний рост в каждой группе:
# - Средний рост футболистов (X1) = (173 + 175 + 180 + 178 + 177 + 185 + 183 + 182) / 8 = 179.25
# - Средний рост хоккеистов (X2) = (177 + 179 + 180 + 188 + 177 + 172 + 171 + 184 + 180) / 9 = 178.33
# - Средний рост штангистов (X3) = (172 + 173 + 169 + 177 + 166 + 180 + 178 + 177 + 172 + 166 + 170) / 11 = 171.36

# 3. Вычислить общую дисперсию:
# - Общая дисперсия (S_total^2) = (Σ(X - X_total)^2) / (N_total) = ((173 - 176.63)^2 + (175 - 176.63)^2 + ... + (170 - 176.63)^2) / 28 = 69.84

# 4. Вычислить факторную дисперсию:
# - Факторная дисперсия (S_factor^2) = ((n1 * (X1 - X_total)^2 + n2 * (X2 - X_total)^2 + n3 * (X3 - X_total)^2) / (k - 1)) = ((8 * (179.25 - 176.63)^2) + (9 * (178.33 - 176.63)^2) + (11 * (171.36 - 176.63)^2)) / (3 - 1) = 2.77

# 5. Вычислить остаточную дисперсию:
# - Остаточная дисперсия (S_residual^2) = (S_total^2 - S_factor^2) = 69.84 - 2.77 = 67.07

# 6. Вычислить F-статистику:
# - F-статистика (F) = (S_factor^2 / (k - 1)) / (S_residual^2 / (N_total - k)) = (2.77 / 2) / (67.07 / 25) = 0.081 / 2.683 = 0.030

# 7. Определить критическое значение F-статистики для выбранного уровня значимости (α) и количества групп (k - 1):
# - Для α = 0.05 и k - 1 = 2, критическое значение F-статистики равно 3.682.

# 8. Сравнить вычисленное значение F-статистики с критическим значением:
# - 0.030 < 3.682, поэтому нет оснований отвергнуть нулевую гипотезу.

# Таким образом, на основании проведенного дисперсионного анализа нет 
# статистически значимых различий в среднем росте между 
# футболистами, хоккеистами и штангистами.

import numpy as np
from scipy import stats

# Заданные значения роста в трех группах спортсменов
footballers = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# Выполняем однофакторный дисперсионный анализ
f_statistic, p_value = stats.f_oneway(footballers, hockey_players, weightlifters)

# Выводим результаты
print("F-статистика:", f_statistic)
print("p-значение:", p_value)