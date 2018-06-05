file = (open('dataset_3363_4.txt').read().lower().replace('\n', ' ').split())
A = [list(map(int, i.split(';')[1:])) for i in file]
C, P, S, T = [], [], [], []
for i in A: C.append(sum(i) / len(i))
for i in A:
    for j in i:
        if j == i[0]:
            P.append(j)
        elif j == i[1]:
            S.append(j)
        else:
            T.append(j)
avr_P = (sum(P) / len(P))
avr_S = (sum(S) / len(S))
avr_T = (sum(T) / len(T))
tot_avr = str(avr_P) + ' ' + str(avr_S) + ' ' + str(avr_T)
with open('solution_4.txt', 'w') as word:
    for i in C: word.writeline(i)
    word.write(str(tot_avr))
