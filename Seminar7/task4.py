# Даны две  независимые выборки. Не соблюдается условие нормальности
# x1  380,420, 290
# y1 140,360,200,900

# Сделайте вывод по результатам, полученным с помощью функции

# Для сравнения двух независимых выборок можно воспользоваться функцией 
# mannwhitneyu из модуля scipy.stats
# Эта функция выполняет непараметрический 
# U-тест Манна-Уитни на сравнение двух выборок. 

from scipy.stats import mannwhitneyu

x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

_, p_value = mannwhitneyu(x1, y1)
alpha = 0.05

if p_value < alpha:
    print("Существуют статистически значимые различия между выборками.")
else:
    print("Нет статистически значимых различий между выборками.")