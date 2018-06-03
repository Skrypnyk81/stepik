import collections as cl
with open('dataset_3363_3.txt') as word:
    S = word.readline().lower().replace('\n', ' ').split()

cnt = cl.Counter()
for word in S:
    cnt[word] += 1
L = sorted(cnt.items(), key = lambda x: x[1], reverse = True)
a = L[0][0], L[0][1]
with open('solution.txt', 'w') as word:
    word.write(str(a))
