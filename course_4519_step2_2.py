'''Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для 
разных интересные ему профессий. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245267/salaries.xlsx. 
Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива после 
его упорядочивания) и, через пробел, название профессии с самой высокой средней зарплатой по всем регионам.'''

import xlrd
from statistics import median, mean
wb = xlrd.open_workbook('salaries.xlsx')
sheet = wb.sheet_by_index(0)
rows = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
columns = [sheet.col_values(colnum) for colnum in range(sheet.ncols)]


def count_max(rows, n):
    dic = {}
    for subjects in rows[1:]:
        dic[subjects[0]] = n(subjects[1:])

    return max(dic, key=dic.get)


print(count_max(rows, median))
print(count_max(columns, mean))
