num_octal = input("Digite um número em notação octal: ")
num_decimal = 0
octal = True

for digito in num_octal:
    if all (digito in '01234567' for digito in num_octal):
        num_decimal  = int(num_octal, 8)
        print (f"O número octal {num_octal} em decimal é {num_decimal}")
        break
    else:
        digito not in '01234567'
        octal = False
        print('Número digitado inválido, digite um número Octal válido')
        break