idade = int(input("Qual é sua idade ? "))
if idade < 16:
    print("Nao-eleitor !")
elif idade >= 18 and idade < 65:
    print("Eleitor obrigatório !")
else: 
    print("Eleitor facultativo !")
    
