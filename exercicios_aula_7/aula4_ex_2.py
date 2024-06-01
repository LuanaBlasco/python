turno = input("Qual turno você trabalha ? (n/d)")
n = "noite"
d = "dia"
horas_trabalhadas = int(input("Qual a quantidade de horas trabalhadas ? "))
hora_trabalhada = 0

if turno == n:
    hora_trabalhada = 45.00
    totaln = horas_trabalhadas*hora_trabalhada
    print("O seu salário será de R$ ", totaln)
else:
    hora_trabalhada = 37.50
    totald = horas_trabalhadas*hora_trabalhada
    print("O seu salário será de R$ ", totald)