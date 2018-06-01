with open('dataset_3363_3.txt') as word:
    S = word.readline().lower().replace('\n', ' ').split()
import collections as cl
cnt = cl.Counter()
for word in S:
    cnt[word] += 1
maximum = max(cnt, key=cnt.get)
print(maximum, cnt[maximum])
