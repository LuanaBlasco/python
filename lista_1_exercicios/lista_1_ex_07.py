print("Investimento com Juros Simples")
vi = float(input("Informe o investimento inicial: "))
tj = float(input("Informe a porcentagem da taxa de juros anual: "))
p = int(input("Digite o período do investimento(em anos): "))
vf = vi + (vi*(tj/100)*p)
print("No período de %i anos, o valor de R$ %.2f passará a ser %.2f considerando os juros simples. " % (p, vi, vf ))