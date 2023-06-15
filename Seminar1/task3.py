# 3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом 
# извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

# Для решения данной задачи можно воспользоваться формулой 
# условной вероятности: вероятность выбрать первую окрашенную 
# деталь будет 9/15, вероятность выбрать вторую окрашенную деталь 
# будет 8/14 (после извлечения первой детали), а вероятность выбрать 
# третью окрашенную деталь будет 7/13 (после извлечения двух первых деталей).
# Таким образом, общая вероятность извлечения трех окрашенных деталей будет:

p = 9/15 * 8/14 * 7/13
print(p)


# Результат выполнения программы: 0.18461538461538457.

# То есть, вероятность того, что рабочий извлечет три 
# окрашенные детали равна 0.1846 (округленно до десятитысячных).