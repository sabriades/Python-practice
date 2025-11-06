lista_uno=input('inserisci prima lista di numeri separati da virgola: ')
lista_due=input('inserisci seconda lista di numeri separati da virgola: ')
lista_uno_str=lista_uno.split(',')
lista_due_str=lista_due.split(',')
lista_uno_num=[]
lista_due_num=[]
for stringa in lista_uno_str:
    try:
        numero=float(stringa)
        lista_uno_num.append(numero)
    except:
        print('non è un numero. sarà ignorato',stringa)

print('lista numerica 1: ', lista_uno_num)

for stringa in lista_due_str:
    try:
        numero=float(stringa)
        lista_due_num.append(numero)
    except:
        print('non è un numero. sarà ignorato',stringa)
print('lista numerica 2: ', lista_due_num)

if len(lista_uno_num)==len(lista_due_num):
    print('stessa lunghezza')
else:
    print('errore')
    exit()
lista_somma=[]
lista_sottrazione=[]
lista_prodotto=[]
lista_divisione=[]
for i in range(len(lista_uno_num)):
        somma=lista_uno_num[i]+lista_due_num[i]
        lista_somma.append(somma)
print('lista somma: ',lista_somma)

for i in range(len(lista_uno_num)):
        sottrazione=lista_uno_num[i]-lista_due_num[i]
        lista_sottrazione.append(sottrazione)
print('lista sottrazione: ',lista_sottrazione)

for i in range(len(lista_uno_num)):
        prodotto=lista_uno_num[i]*lista_due_num[i]
        lista_prodotto.append(prodotto)
print('lista prodotto: ',lista_prodotto)

for i in range(len(lista_uno_num)):
    if lista_due_num[i]==0:
        print('non è possibile dividere per zero')
        lista_divisione.append(None)
    else:
        divisione=lista_uno_num[i]/lista_due_num[i]
        lista_divisione.append(divisione)
print('lista divisione: ',lista_divisione)