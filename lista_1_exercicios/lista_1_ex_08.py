print("Investimento com Juros Compostos")
vi = float(input("Informe o investimento inicial: "))
tj = float(input("Informe a porcentagem da taxa de juros anual: "))
p = int(input("Digite o período do investimento(em anos): "))
vf = vi * (1+ (tj/100))**p
print("No período de %i anos, o valor de R$ %.2f passará a ser %.2f considerando os juros compostos. " % (p, vi, vf ))