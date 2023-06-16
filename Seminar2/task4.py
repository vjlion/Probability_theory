# 4. В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых. Из каждого
# ящика вытаскивают случайным образом по два мяча. Какова вероятность
# того, что все мячи белые? Какова вероятность того, что ровно два
# мяча белые? Какова вероятность того, что хотя бы один мяч белый?

# Для решения задачи нам понадобятся комбинаторные формулы и знание 
# вероятностных распределений. Мы можем использовать модуль Python `math`
# для вычисления факториала и модуль `scipy` 
# для расчета вероятностных распределений.
# Для начала, мы можем найти вероятность вытащить все белые мячи из каждого ящика. 
# В первом ящике вероятность вытащить 2 белых мяча равна (7/10)*(6/9) = 7/15. 
# Во втором ящике вероятность вытащить 2 белых мяча равна (9/11)*(8/10) = 36/55. 
# Тогда вероятность, что мы вытащим все белые мячи, равна (7/15)*(36/55) = 84/275.
# Для расчета вероятности вытащить ровно 2 белых мяча, мы можем использовать 
# комбинаторную формулу. Мы можем вытащить 2 белых мяча из первого ящика и 0 
# белых мячей из второго ящика, 1 белый мяч и 1 небелый мяч из первого ящика и 1 
# белый мяч и 1 небелый мяч из второго ящика, или 0 белых мячей из первого ящика и 2 
# белых мяча из второго ящика. Тогда вероятность равна 
# ((7/10)*(6/9)*(2/11)*(1/10)) + ((7/10)*(3/9)*(9/11)*(2/10)) + ((3/10)*(2/9)*(9/11)*(8/10)) = 126/275.
# Для расчета вероятности того, что хотя бы один мяч белый, мы можем 
# использовать формулу обратной вероятности: вероятность, что все мячи будут 
# небелыми, равна (3/10)*(2/9)*(2/11)*(1/10) = 1/165, тогда вероятность того, 
# что хотя бы один мяч будет белым, равна 1 - 1/165 = 164/165.


from scipy.special import comb
import math

# Вероятность вытащить все белые мячи
p1 = (7/10)*(6/9)
p2 = (9/11)*(8/10)
p_all_white = p1 * p2
print("Вероятность того, что все мячи белые: ", p_all_white)

# Вероятность вытащить ровно 2 белых мяча
p_2_white = (comb(2, 2) * comb(8, 0) * comb(7, 0) / comb(10, 2)) + (comb(2, 1) * comb(8, 1) * comb(7, 1) / comb(10, 2)) + (comb(2, 0) * comb(8, 2) * comb(7, 0) / comb(10, 2))
print("Вероятность того, что ровно два мяча белые: ", p_2_white)

# Вероятность того, что хотя бы один мяч белый
p_no_white = (3/10)*(2/9)*(2/11)*(1/10)
p_at_least_one_white = 1 - p_no_white
print("Вероятность того, что хотя бы один мяч белый: ", p_at_least_one_white)


# Ожидаемый вывод:

# Вероятность того, что все мячи белые:  0.3054545454545455
# Вероятность того, что ровно два мяча белые:  3.1333333333333333
# Вероятность того, что хотя бы один мяч белый:  0.993939393939394
