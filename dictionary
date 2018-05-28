def update_dictionary(d, key, value):
    # put your python code here
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key] = []
        d[2*key].append(value)
d = {}
print(update_dictionary(d, 1, -1))
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
