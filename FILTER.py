numeri=input('inserisci numeri separati da virgola: ')
lista_stringhe=numeri.split(',')
lista_numeri=[]
positivi=[]
negativi=[]
zeri=[]
for stringa in lista_stringhe:
    try:
        numero=float(stringa)
        lista_numeri.append(numero)
        if numero>0:
            positivi.append(numero)
        elif numero<0:
            negativi.append(numero)
        elif numero==0:
            zeri.append(numero)
    except:
        print('verrà ignorato: '+stringa)

print('numeri positivi: '+str(positivi))
print('numeri positivi è lunga: '+str(len(positivi)))
print('numeri negativi: '+str(negativi))
print('numeri negativi è lunga: '+str(len(negativi)))
print('zeri: '+str(zeri))
print('zeri è lunga: '+str(len(zeri)))
