# Проведено 4 эксперимента. Для каждого построить график и посчитать коэффициенты
# корреляции Пирсона.
# x = np.array([10,8, 13, 9,11,14, 6,4,12, 7,5])
# y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68 ])
# x= np.array([ 10,8, 13, 9,11,14, 6,4,12, 7,5 ])
# y2 = np.array([ 9.14, 8.14, 8.74,8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
# x= np.array([ 10,8, 13, 9,11,14, 6,4,12, 7,5 ])
# y3 = np.array([7.46,6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
# x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
# y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25,12.5, 5.56, 7.91, 6.89])
# x0= np.array([ 10, 8, 13, 9, 11, 14, 6, 4, 12, 7,5, 15, 16, 18 ])
# y0 = np.array([ 9.14, 8.14, 8.74,8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74, 6.5, 5, 2.9])
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

x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

x2 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])

x3 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])

x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89])

x5 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5, 15, 16, 18])
y5 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74, 6.5, 5, 2.9])

plt.subplot(231)
plt.scatter(x1, y1)
plt.title('Experiment 1')
coef1, pval1 = stats.pearsonr(x1, y1)
plt.xlabel('x')
plt.ylabel('y')
plt.text(4, 11, f'r={coef1:.2f}')

plt.subplot(232)
plt.scatter(x2, y2)
plt.title('Experiment 2')
coef2, pval2 = stats.pearsonr(x2, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.text(4, 11, f'r={coef2:.2f}')

plt.subplot(233)
plt.scatter(x3, y3)
plt.title('Experiment 3')
coef3, pval3 = stats.pearsonr(x3, y3)
plt.xlabel('x')
plt.ylabel('y')
plt.text(4, 11, f'r={coef3:.2f}')

plt.subplot(234)
plt.scatter(x4, y4)
plt.title('Experiment 4')
coef4, pval4 = stats.pearsonr(x4, y4)
plt.xlabel('x')
plt.ylabel('y')
plt.text(4, 11, f'r={coef4:.2f}')

plt.subplot(235)
plt.scatter(x5, y5)
plt.title('Experiment 5')
coef5, pval5 = stats.pearsonr(x5, y5)
plt.xlabel('x')
plt.ylabel('y')
plt.text(4, 11, f'r={coef5:.2f}')

plt.tight_layout()
plt.show()