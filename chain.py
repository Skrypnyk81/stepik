import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
cont = 0
A = '699991.txt'
while True:
    print(A)
    r = requests.get(url + A)
    A = r.text
    cont += 1
    print(cont)
    if r.text.startswith('We'): break
print(r.text)
