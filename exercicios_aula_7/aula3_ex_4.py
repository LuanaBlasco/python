valorPrestacao = float(input("Qual o valor da prestação ? "))
multa = int(input("Qual a porcentagem da multa ?(Digite somente números) "))
qtdDias = int(input("Quantos dias está em atraso ? "))
prestacao = valorPrestacao + (valorPrestacao*(multa/100)*qtdDias)
print("O valor atualizado da prestação + os acrèscimos por multa é de R$ ", prestacao)