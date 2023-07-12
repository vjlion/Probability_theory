# Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
# регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
# линейной регрессии.
# X1= np.array([30,30,40, 40)]
# Y1= np.array([37, 47, 50, 60)]
# x2= np.array([30,30,40, 40, 20, 20, 50, 50])
# y2= np.array([37, 47, 50, 60, 25, 35, 62, 72])
# X3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
# Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84]) 
# import scipy.stats as stats
# import numpy as np
# import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.title('r= вписать значение коэффициента')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([30, 30, 40, 40])
Y1 = np.array([37, 47, 50, 60])
x2 = np.array([30, 30, 40, 40, 20, 20, 50, 50])
y2 = np.array([37, 47, 50, 60, 25, 35, 62, 72])
X3 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

# Найдем коэффициенты для линии регрессии
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(X1, Y1)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x2, y2)
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(X3, Y3)

# Найдем коэффициенты детерминации
r_squared1 = r_value1**2
r_squared2 = r_value2**2
r_squared3 = r_value3**2

# Построим графики
plt.scatter(X1, Y1)
plt.plot(X1, intercept1 + slope1*X1, 'r', label='Линейная регрессия')
plt.title(f'r={r_value1:.2f}, R^2={r_squared1:.2f}')
plt.xlabel('X1')
plt.ylabel('Y1')
plt.legend()
plt.show()

plt.scatter(x2, y2)
plt.plot(x2, intercept2 + slope2*x2, 'r', label='Линейная регрессия')
plt.title(f'r={r_value2:.2f}, R^2={r_squared2:.2f}')
plt.xlabel('x2')
plt.ylabel('y2')
plt.legend()
plt.show()

plt.scatter(X3, Y3)
plt.plot(X3, intercept3 + slope3*X3, 'r', label='Линейная регрессия')
plt.title(f'r={r_value3:.2f}, R^2={r_squared3:.2f}')
plt.xlabel('X3')
plt.ylabel('Y3')
plt.legend()
plt.show()