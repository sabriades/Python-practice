totale_conto=input('totale del conto: ')
percentuale_di_mancia=input('percentuale di mancia: ')

if percentuale_di_mancia=='':
    percentuale_di_mancia=10
    print('percentuale di mancia default: '+str(percentuale_di_mancia))
else:
    percentuale_di_mancia=float(percentuale_di_mancia)

mancia=float(totale_conto)*(float(percentuale_di_mancia)/100)

if mancia<2:
    print('mancia troppo bassa')
totale_finale=float(totale_conto)+mancia

print('importo del conto: '+str(totale_conto)+'€')
print('mancia: '+str(round(mancia,2))+'€')
print('totale finale: '+str(totale_finale)+'€')