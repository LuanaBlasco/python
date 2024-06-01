sal_fixo = float(input("Qual seu salário fixo ? R$ "))
vendas = float(input("Qual foi o valor de suas vendas ? R$ "))
comissao = vendas * 0.04
total_comissao = vendas + comissao
total = sal_fixo + total_comissao
print("O valor total de seu salário de %.2f + as vendas de %.2f com a comissão é de R$ %.2f " % (sal_fixo, vendas, total))