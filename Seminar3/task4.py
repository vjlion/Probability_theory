# В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, 
# а для студента факультета C - 0.9. Студент сдал первую сессию. 
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?


# вероятность того, что случайно выбранный студент учится на факультете A
P_A = 1/4

# вероятность того, что случайно выбранный студент учится на факультете B
P_B = 1/4

# вероятность того, что случайно выбранный студент учится на факультете C
P_C = 1/2

# вероятность того, что случайно выбранный студент сдал первую сессию
P_P = P_A * 0.8 + P_B * 0.7 + P_C * 0.9

# вероятность того, что студент учится на факультете A, если он сдал первую сессию
P_A_P = P_A * 0.8 / P_P

# вероятность того, что студент учится на факультете B, если он сдал первую сессию
P_B_P = P_B * 0.7 / P_P

# вероятность того, что студент учится на факультете C, если он сдал первую сессию
P_C_P = P_C * 0.9 / P_P

# вывод результатов
print("Вероятность того, что студент, сдавший первую сессию, учится:")
print("а) на факультете А: {:.2f}".format(P_A_P))
print("б) на факультете B: {:.2f}".format(P_B_P))
print("в) на факультете C: {:.2f}".format(P_C_P))


# Результат выполнения программы:

# Вероятность того, что студент, сдавший первую сессию, учится:
# а) на факультете А: 0.24
# б) на факультете B: 0.21
# в) на факультете C: 0.55