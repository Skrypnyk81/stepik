with open('dataset_3363_2.txt') as inf:
    S =inf.readline().strip()
C, D, N = [], [], []
for i in S:
	if i.isdigit():
		D.append(i)
	else:
		if D:
			N.append(int("".join(D)))
			D = []
		C.append(i)
N.append(int("".join(D)))
Sol=(''.join(c * n for c, n in zip(C, N)))

with open('solution.txt', 'w') as ouf:
    ouf.write(Sol)
