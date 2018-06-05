s = input()
x, c, = 1, 1
j = s[x:x + 1]
for i in s:
    if i in j:
        c += 1
    else:
        print(i, end = '')
        print(c, end ='')
        c = 1
    x += 1
    j = s[x:x + 1]
