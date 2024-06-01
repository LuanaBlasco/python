num_hex = input("Digite um número Hexadecimal: ")
num_decimal = 0
hexadecimal = True

verif_hexa = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}


for digito in num_hex:
    if all (digito.lower() in verif_hexa for digito in num_hex):
        num_decimal = int(num_hex, 16)
        print(f'O número hexadecima {num_hex} convertido em Decimal é {num_decimal}')
        break
    else:
        digito not in verif_hexa
        hexadecimal = False
        print('O número digitado não é válido, digite um número na notação hexadecimal válido')
        break
