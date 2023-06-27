# Даны значения зарплат из выборки выпускников: 
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.


import math

# Зарплаты из выборки
data = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Расчет среднего арифметического
mean = sum(data) / len(data)
print("Среднее арифметическое:", mean)

# Расчет среднего квадратичного отклонения
dev = [(x - mean)**2 for x in data]
stdev = math.sqrt(sum(dev) / len(data))
print("Среднее квадратичное отклонение:", stdev)

# Расчет смещенной и несмещенной оценок дисперсии
variance = sum(dev) / len(data) # смещенная оценка дисперсии
unbiased_var = sum(dev) / (len(data) - 1) # несмещенная оценка дисперсии
print("Смещенная оценка дисперсии:", variance)
print("Несмещенная оценка дисперсии:", unbiased_var)


# Ответ:
# Среднее арифметическое: 65.3
# Среднее квадратичное отклонение: 30.823854398825596
# Смещенная оценка дисперсии: 950.11
# Несмещенная оценка дисперсии: 1000.1157894736842