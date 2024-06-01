carneirinhos = 0
while True:
    sono = input("Já dormi? (sim/não) ")
    if sono == "sim" or sono == "SIM" or sono == "Sim":
        print("Carneirinhos contados = ", carneirinhos)
        break
    else:
        carneirinhos += 1
        print("Carneirinhos contados = ", carneirinhos)

