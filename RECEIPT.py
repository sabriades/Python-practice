price=input('price: ')

if float(price)<0:
    print("error: the price cannot be negative")

quantity=input('quantity: ')
discount_percentage=input('discount percentage (%): ')

VAT_rate=input('IVA rate: ') #aliquota IVA

if VAT_rate=='':
    VAT_rate=22
else:
    VAT_rate=float(VAT_rate)

subtotal=float(price)*float(quantity)
discount=float(subtotal)*(float(discount_percentage)/100)
taxable=float(subtotal)-discount
VAT=taxable*(float(VAT_rate)/100)
total=taxable+VAT

print('subtotal:'+str(subtotal)+'€')
print('discount: '+str(discount)+'€')
print('taxable: '+str(taxable)+'€')
print('VAT: '+str(VAT)+'€')

if total>=100:
    print('free shipping')
else:
    print('shipping: 5.00€')
  #  total_ship=total+5
    total += 5
    print('total with shipping: '+str(total)+'€')


