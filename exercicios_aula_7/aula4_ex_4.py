agua = float(input("Qual é o valor da conta de água ? R$ "))
luz = float(input("Qual é o valor da conta de luz ? R$ "))
telefone = float(input("Qual é o valor da conta de telefone ? R$ "))
sal = float(input("Qual é o valor do seu salário ? R$ "))
total_contas = agua + luz + telefone
if sal > total_contas:
    print("Contas serão pagas")
    total = sal - total_contas
    print("Restou R$ %f de seu salário !" % (total))
else:
    print("Salário insuficiente!")

