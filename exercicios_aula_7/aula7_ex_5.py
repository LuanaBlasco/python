sexo = input("Qual seu sexo ? (f/m) ")
altura = float(input("Qual sua altura em metros ? "))
peso = float(input("Quantos kg você pesa ? "))
ideal = 0

# Verificar o sexo e calcular o peso ideal
if sexo == "f" or sexo == "F":
    ideal = (62.1 * altura) - 44.7
    # Comparar o peso com o peso ideal
    if peso > ideal:
        print("GORDA!")
    elif peso < ideal:
        print("DESNUTRIDA !")
    else:
        print("Peso ideal !")
elif sexo == "m" or sexo == "M":
    ideal = (72.7 * altura) - 58
    # Comparar o peso com o peso ideal
    if peso > ideal:
        print("GORDO!")
    elif peso < ideal:
        print("DESNUTRIDO !!")
    else:
        print("Peso ideal !")
else:
    print("Sexo desconhecido")

print("O peso ideal seria: ", ideal)














# sexo = input("Qual seu sexo ? (f/m) ")
# altura = float(input("Qual sua altura em metros ? "))
# peso = float(input("Quantos kg você pesa ? "))
# ideal = 0
# if sexo == "f" or sexo == "F":
#     ideal = (62.1*altura) - 44.7
# elif sexo == "m" or sexo == "M":
#     ideal = (72.7*altura)-58 
# else:
#     print("Sexo desconhecido")
#     sexo = None
    

# if peso > ideal:
#     print("GORDA!")
# elif peso < ideal:
#     print("DESNUTRIDA !")
# else:
#     peso == ideal
#     print("Peso ideal !")

# print("O peso ideal seria: ", ideal)
