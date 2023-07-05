# Даны значения проницаемости сосудов сетчатки gr1 (здоровые пациенты), gr 2 ( поражение в области центральной
# ямки), gr3 (в области центральной ямки и на периферии).
# Сравнить данные, относящиеся к разным видам поражения.
# gr1 =([0.5, 0.7, 1, 1.2, 1.4])
# gr2 = ([1.3, 1.45, 1.6, 1.7, 1.8])
# gr3 = ([6.2, 12.6, 13.2, 14.1, 14.2])

from scipy.stats import kruskal

gr1 = [0.5, 0.7, 1, 1.2, 1.4]
gr2 = [1.3, 1.45, 1.6, 1.7, 1.8]
gr3 = [6.2, 12.6, 13.2, 14.1, 14.2]

statistic, p_value = kruskal(gr1, gr2, gr3)

print("Статистика теста:", statistic)
print("p-значение:", p_value)

if p_value < 0.05:
    print("Существует статистически значимая разница между группами.")
else:
    print("Нет статистически значимой разницы между группами.")


# Тест Крузкала-Уоллиса проверяет наличие статистически значимой 
# разницы между группами на основе ранговых данных. 
# Аналогично тесту Фридмана, p-значение меньше выбранного уровня значимости (обычно 0.05) 
# указывает на статистически значимую разницу между группами.