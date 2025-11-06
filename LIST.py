input_numeri=input('inserisci numeri separati da virgola: ')
lista_stringhe=input_numeri.split(',')
lista_numeri=[]

for stringa in lista_stringhe:
    try:
        numero=float(stringa)
        lista_numeri.append(numero)
    except:
        print('valore non valido ignorato: '+stringa)

if not lista_numeri:
    print('nessun numero inserito')
    exit()

print(lista_numeri)

print('lunghezza della lista: '+str(len(lista_numeri)))
print('somma dei numeri: '+str(sum(lista_numeri)))
print('massimo valore: '+str(max(lista_numeri)))
print('minimo valore: '+str(min(lista_numeri)))
media=round((sum(lista_numeri)/len(lista_numeri)),2)
print('media: '+str(media))

