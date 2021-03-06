"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с 
указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта. Ему не удалось 
найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю). 
Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. 
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx 

Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и его количества 
в граммах. Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов. Числа округлите до целых вниз 
и введите через пробел.
"""

import pandas as pd

file = pd.read_excel('C:/Users/Murchik/Prova/trekking2.xlsx')
second_sheet = pd.read_excel('C:/Users/Murchik/Prova/trekking2.xlsx', sheet_name='Раскладка')

corr_file = file.fillna(0)

dic = {}
for index, row in corr_file.iterrows():
    dic[row[0]] = [row[1], row[2], row[3], row[4]]
    
lst = []
for index, row in second_sheet.iterrows():
    lst.append([x * (row[1]/100) for x in dic[row[0]]])

[sum(x) for x in zip(*lst)]
