h = float(input("Qual o valor da altura do tronco da pirâmide ? "))
bmenor = float(input("Qual o valor da base menor ? "))
bmaior = float(input("Qual o valor da base maior ? "))
volume = h/3 * (bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2)**0.5)
print("O volume do tronco da pirâmide é: ", volume)
