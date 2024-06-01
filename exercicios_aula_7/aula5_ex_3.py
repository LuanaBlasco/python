produto = input("Digite nome do produto: ")
valor = float(input("Digite o valor da compra: "))
if valor < 10:
    lucro1 = valor * 0.7
    valor_venda1 = valor + lucro1
    print("O produto vendido foi %s e o lucro foi %f" % (produto, valor_venda1))
elif valor <= 10 and valor < 30:
    lucro2 = valor * 0.5
    valor_venda2 = valor + lucro2
    print("O produto vendido foi %s e o lucro foi %f" % (produto, valor_venda2))
elif valor <= 30 and valor < 50:
    lucro3 = valor * 0.4
    valor_venda3 = valor + lucro3
    print("O produto vendido foi %s e o lucro foi %f" % (produto, valor_venda3))
else:
    lucro4 = valor * 0.3
    valor_venda4 = valor + lucro4
    print("O produto vendido foi %s e o lucro foi %f" % (produto, valor_venda4))
