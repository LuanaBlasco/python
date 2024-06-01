num_binario = input("Digite um número binário: ")
num_decimal = 0
binario = True

lista_num = list(num_binario)

for digito in num_binario:
    if all (digito in '01' for digito in lista_num):
        num_decimal = int(num_binario, 2)
        print(f" O número binário {num_binario} em decimal é {num_decimal}")
        break
    else:
        digito not in '01'
        binario = False
        print("O número digitado não é binário, digite um número binário válido")
    
