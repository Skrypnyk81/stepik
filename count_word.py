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

#in two strings without sort   
from collections import Counter
print('\n'.join(f'{w} {n}' for w, n in Counter(open('dataset_3363_3.txt').read().lower().split()).most_common()), file=open('out', 'w'))
