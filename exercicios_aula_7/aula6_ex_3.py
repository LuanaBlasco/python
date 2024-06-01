n = int(input("Digite um valor: "))
s=0
if n <0:
    print("O número deverá ser positivo !")
else:
    for i in range(1, n+1):
        s+=1/i
    print("A soma das frações até %i é %f " % (n, s))


