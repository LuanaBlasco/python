compra = float(input("Qual o valor da compra ? R$ "))
if compra > 200:
    desc = compra * 0.2
    total = compra - desc
    print("Você tem direito a desconto ! O novo valor é de R$ %f " % (total))
else:
    print("Não tem desconto sobre esse valor, o valor total é de  R$ %f " % compra)