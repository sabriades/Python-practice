numeri=input('inserisci numeri separati da virgola: ')
lista_stringhe=numeri.split(',')
lista_numeri=[]
for stringa in lista_stringhe:
    try:
        numero=float(stringa)
        lista_numeri.append(numero)
    except:
        print('non è un numero. sarà ignorato')

if not lista_numeri:
    print('lista vuota: errore')
    exit()

no_dupes=list(set(lista_numeri))
lista_crescente=sorted(no_dupes)
lista_decrescente=sorted(no_dupes, reverse=True)
dupes_rimossi=len(lista_numeri)-len(no_dupes)
print('lista dei numeri: ', lista_numeri)
print('lista crescente: ', lista_crescente)
print('lista decrescente: ', lista_decrescente)
print('lista senza duplicati: ', no_dupes)
print('duplicati rimossi: ', dupes_rimossi)