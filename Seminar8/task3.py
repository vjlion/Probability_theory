# Используя функцию stats.ttest_ind, проведите односторонний
# тест. Проверить ,что мю 1 > мю 2
# stats.ttest_ind(a, b,alternative='greater', equal_var = True)

from scipy import stats

# your data for sample a
a = [1, 2, 3, 4, 5]

# your data for sample b
b = [6, 7, 8, 9, 10]

# conduct one-sided t-test
t_statistic, p_value = stats.ttest_ind(a, b, alternative='greater', equal_var=True)

# output the results
print("T-statistic:", t_statistic)
print("P-value:", p_value)