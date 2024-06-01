valores= [1,4,-3,5,-7,-9,-1,10]
positivos = 0
negativos = 0
menor = valores[0]

for valor in valores:
    if valor > 0:
        positivos = positivos + 1
    elif valor < 0:
        negativos = negativos + 1
        if valor < menor:
            menor = valor

print(valores)
print(len(valores))
print("Número de valores positivos: ", positivos)
print("Número de valores negativos: ", negativos)
print("O menor valor é: ", menor)
            
