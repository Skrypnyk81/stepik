"""Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью, у него сохранились расчётные листки всех сотрудников. 
Помогите по этим расчётным листкам восстановить зарплатную ведомость. Архив с расчётными листками доступен по ссылке 
https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip (вы можете скачать и распаковать его вручную или самостоятельно научиться делать это 
с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата. Сотрудники должны быть упорядочены по алфавиту.
"""




import pandas as pd

df = pd.DataFrame(columns=['col1','col2'])

for file in range(1,1001):
    source = pd.read_excel('rogaikopyta/{}.xlsx'.format(file))
    res = source.iloc[0][1],source.iloc[0][3]
    df = df.append({'col1': res[0], 'col2': res[1]}, ignore_index=True)
    
sort_df = df.sort_values(['col1'])

sort_df["col2"] = sort_df["col2"].astype(float).astype(int)

with open('answer.txt', 'w',  encoding='utf-8') as f:
    for ind in sort_df.index:
        a = str(sort_df['col1'][ind]) + ' '
        b = str(sort_df['col2'][ind]) + '\n'
        f.write(a)
        f.write(b)
