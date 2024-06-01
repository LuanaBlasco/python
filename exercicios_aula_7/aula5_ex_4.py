n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1/n2
escolha = input("Qual função deseja entre os numeros que digitou ? (soma, sub, mult ou div ?)")

if escolha == "soma":
    print ("A soma entre %.2f e %.2f é %.2f " % (n1, n2, soma))
elif escolha == "sub":
    print("A subtração entre %.2f e %.2f é %.2f " % (n1, n2, sub))
elif escolha == "mult":
    print("A multiplicação entre %.2f e %.2f é %.2f " % (n1, n2, mult))
else:
    print("A divisão entre %f e %f é %f " %(n1, n2, div))
