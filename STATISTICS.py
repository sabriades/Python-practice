frase=input('inserisci una frase: ')
frase=frase.lower()
lista_parole=frase.split()
print('numero di parole nella frase: ',len(lista_parole))
frequenza={}
lista_caratteri=[]
for carattere in frase:
    if carattere.isalpha(): #se un carattere è alfabetico
        lista_caratteri.append(carattere)
        if carattere in frequenza:
            frequenza[carattere] +=1
        else:
            frequenza[carattere]=1
#print('frequenza dei caratteri: ',frequenza)
print('frequenza dei caratteri in ordine alfabetico: ')
for lettera in sorted(frequenza.keys()):
    print(lettera,': ', frequenza[lettera])
print('numero dei caratteri senza spazi: ', len(lista_caratteri))
print('numero dei caratteri con spazi: ', len(frase))