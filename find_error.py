'''

Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d d d известных нам слов, после чего на d d d строках указываются эти слова. Затем передаётся количество l l l строк текста для проверки, после чего l l l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the

'''

n1 = int(input())
lst1 = []
for i in range(n1):
  lst1.append(input().lower())

n2 = int(input())
lst2 = []
for i in range(n2):
  lst2.append(input().lower().split())

result = []
for i in lst2:
    for word in i:
        if word in lst1:
            pass
        else:
            result.append(word)
    
print('\n'.join(set(result)))
