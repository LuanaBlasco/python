while True:
    opcao = input("Escolha qual conversão deseja: \n[1] Converter Binário para Decimal, \n[2] Converter Octal para Decimal, \n[3] Converter Hexadecimal para Decimal, ou \n[4] para Sair: ")

    if opcao == '1':
        num_binario = input("Digite um número binário: ")
        num_decimal = 0
        binario = True
        for digito in num_binario:
            if all (digito in '01' for digito in num_binario):
                num_decimal = int(num_binario, 2)
                print(f" O número BINÁRIO {num_binario} convertido em DECIMAL é {num_decimal}")
                break
            else:
                digito not in '01'
                binario = False
                print("O número digitado não é binário, digite um número binário válido")
                break
    elif opcao == '2':
        num_octal = input("Digite um número em notação octal: ")
        num_decimal = 0
        octal = True
        for digito in num_octal:
            if all (digito in '01234567' for digito in num_octal):
                num_decimal  = int(num_octal, 8)
                print (f"O número OCTAL {num_octal} convertido em DECIMAL é {num_decimal}")
                break
            else:
                digito not in '01234567'
                octal = False
                print('Número digitado inválido, digite um número Octal válido')
                break
    elif opcao == '3':
        num_hex = input("Digite um número Hexadecimal: ")
        num_decimal = 0
        hexadecimal = True
        verif_hexa = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
        for digito in num_hex:
            if all (digito.lower() in verif_hexa for digito in num_hex):
                num_decimal = int(num_hex, 16)
                print(f'O número HEXADECIMAL {num_hex} convertido em DECIMAL é {num_decimal}')
                break
            else:
                digito not in verif_hexa
                hexadecimal = False
                print('O número digitado não é válido, digite um número na notação hexadecimal válido')
                break
    else:
        print("Obrigada por usar a calculadora de conversão de bases da Luana! ")
        break