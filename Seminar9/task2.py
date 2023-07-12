# X3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
# Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84]) 
# Оценить статистическую значимость полученной модели линейной регрессии с помощью Критерия Фишера

from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import numpy as np

X3 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60]).reshape((-1, 1))
Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

X3 = sm.add_constant(X3)  # Добавляем константу для оценки коэффициента сдвига

model = sm.OLS(Y3, X3)
results = model.fit()

f_value = results.fvalue
p_value = results.f_pvalue

print('F-статистика:', f_value)
print('p-значение:', p_value)