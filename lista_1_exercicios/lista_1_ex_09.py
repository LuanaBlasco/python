print("Cálculo de Desconto em Compras")
tot = float(input("Informe o valor total da compra: R$ "))
perc_desc = int(input("Informe a porcentagem do desconto a ser aplicado(somente números): "))
desc = tot *( perc_desc/100)
vf = tot - desc
print("A compra de R$ %.2f com desconto de R$ %.2f fica R$ %.2f " % (tot, desc, vf))
