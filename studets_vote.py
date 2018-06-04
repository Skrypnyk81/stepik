file = (open('dataset_3363_4.txt').read().lower().replace('\n', ' ').split())
A = [list(map(int, i.split(';')[1:])) for i in file]
C = []
for i in A:
    C.append(sum(i) / len(i))
print(C)
with open('solution_4.txt', 'w') as word:
    word.write(str(C))
