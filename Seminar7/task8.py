# Заявляется, что партия изготавливается со средним арифметическим 2,5 см. 
# Проверить данную гипотезу, если известно, что размеры изделий подчинены 
# нормальному закону распределения. Объем выборки 10,
# уровень статистической значимости 5%

# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

# Для проверки гипотезы о среднем значении изделий с 
# спользованием нормального закона распределения,
# мы можем воспользоваться функцией zscore из модуля scipy.stats 
# и сравнить полученное Z-значение со значением критической области 
# стандартного нормального распределения при выбранном уровне значимости.

from scipy.stats import norm
import numpy as np

sample = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
mean_hypothesis = 2.5
alpha = 0.05

sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
z_value = (sample_mean - mean_hypothesis) / (sample_std / np.sqrt(len(sample)))

critical_value = norm.ppf(1 - alpha)

if z_value > critical_value:
    print("Отвергаем гипотезу о среднем значении 2.5 см.")
else:
    print("Принимаем гипотезу о среднем значении 2.5 см.")