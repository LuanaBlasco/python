while True:
    opcao = input("Escolha qual conversão deseja: \n[1] Converter Binário para Decimal, \n[2] Converter Octal para Decimal, \n[3] Converter Hexadecimal para Decimal, \n[4] Converter Decimal para Binário, \n[5] Converter Decimal para Octal, \n[6] Converter Decimal para Hexadecimal ou \n[7] para Sair: ")

    if opcao == '1':
        num_binario = input("Digite um número binário: ")
        num_decimal = 0
        binario = True
        for digito in num_binario:
            if all (digito in '01' for digito in num_binario):
                num_decimal = int(num_binario, 2)
                print(f" O número binário {num_binario} em decimal é {num_decimal}")
                break
            else:
                digito not in '01'
                binario = False
                input("O número digitado não é binário, digite um número binário válido.")      
                break      
    elif opcao == '2':
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
    elif opcao == '3':
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
    elif opcao == '4':
        num_decimal = int(input('Digite um número decimal: '))
        print("O número decimal {} convertido para BINÁRIO é igual a {}".format(num_decimal, bin(num_decimal)[2:]))
    elif opcao == '5':
        num_decimal = int(input('Digite um número decimal: '))
        print("O número decimal {} convertido para OCTAL é igual a {}".format(num_decimal, oct(num_decimal)[2:]))
    elif opcao == '6':
        num_decimal = int(input('Digite um número decimal: '))
        print("O número decimal {} convertido para HEXADECIMAL é igual a {}".format(num_decimal, hex(num_decimal)[2:]))
    else:
        print("Obrigada por usar a calculadora de conversão de bases ! ")
        break


