youtuber_a = "Roberta Viradona"
youtuber_b = "Pacheco X9"
youtuber = [youtuber_a, youtuber_b]

visualizacoes_a = []
visualizacoes_b = []
visualizacoes = [visualizacoes_a, visualizacoes_b]

print("Mês 0")
visualizacoes[0].append(1)
visualizacoes[1].append(1)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][0]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][0]}")

print("Mês 1")
visualizacoes[0].append(10)
visualizacoes[1].append(10)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][1]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][1]}")

diferenca_a = visualizacoes[0][1] - visualizacoes[0][0]
diferenca_b = visualizacoes[1][1] - visualizacoes[1][0]
if diferenca_a > diferenca_b:
    print(f"O canal {youtuber[0]} teve {diferenca_a-diferenca_b} visualizações a mais do que o canal {youtuber[1]}")
elif diferenca_a < diferenca_b:
    print(f"O canal {youtuber[1]} teve {diferenca_b-diferenca_a} visualizações a mais do que o canal {youtuber[0]}")
else:
    print("Os canais tiveram a mesma quantidade de visualizações.")

taxa_crescimento_a = diferenca_a / visualizacoes[0][0]
taxa_crescimento_b = diferenca_b / visualizacoes[1][0]
if taxa_crescimento_a > taxa_crescimento_b:
    print(f"O canal {youtuber[0]} cresceu {taxa_crescimento_a / taxa_crescimento_b} vezes mais do que o canal {youtuber[1]} em termos de visualizações.")
elif taxa_crescimento_a < taxa_crescimento_b:
    print(f"O canal {youtuber[1]} cresceu {taxa_crescimento_b / taxa_crescimento_a} vezes mais do que o canal {youtuber[0]} em termos de visualizações.")
else:
    print("Os canais tiveram o mesmo crescimento em termos de visualizações.")

print("Mês 2")
visualizacoes[0].append(1000)
visualizacoes[1].append(500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][2]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][2]}")

diferenca_a = visualizacoes[0][2] - visualizacoes[0][1]
diferenca_b = visualizacoes[1][2] - visualizacoes[1][1]
if diferenca_a > diferenca_b:
    print(f"O canal {youtuber[0]} teve {diferenca_a-diferenca_b} visualizações a mais do que o canal {youtuber[1]}")
elif diferenca_a < diferenca_b:
    print(f"O canal {youtuber[1]} teve {diferenca_b-diferenca_a} visualizações a mais do que o canal {youtuber[0]}")
else:
    print("Os canais tiveram a mesma quantidade de visualizações.")

taxa_crescimento_a = diferenca_a / visualizacoes[0][1]
taxa_crescimento_b = diferenca_b / visualizacoes[1][1]
if taxa_crescimento_a > taxa_crescimento_b:
    print(f"O canal {youtuber[0]} cresceu {taxa_crescimento_a / taxa_crescimento_b} vezes mais do que o canal {youtuber[1]} em termos de visualizações.")
elif taxa_crescimento_a < taxa_crescimento_b:
    print(f"O canal {youtuber[1]} cresceu {taxa_crescimento_b / taxa_crescimento_a} vezes mais do que o canal {youtuber[0]} em termos de visualizações.")
else:
    print("Os canais tiveram o mesmo crescimento em termos de visualizações.")


print("Mês 3")
visualizacoes[0].append(2000)
visualizacoes[1].append(1500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][3]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][3]}")

diferenca_a = visualizacoes[0][3] - visualizacoes[0][2]
diferenca_b = visualizacoes[1][3] - visualizacoes[1][2]
if diferenca_a > diferenca_b:
    print(f"O canal {youtuber[0]} teve {diferenca_a-diferenca_b} visualizações a mais do que o canal {youtuber[1]}")
elif diferenca_a < diferenca_b:
    print(f"O canal {youtuber[1]} teve {diferenca_b-diferenca_a} visualizações a mais do que o canal {youtuber[0]}")
else:
    print("Os canais tiveram a mesma quantidade de visualizações.")

taxa_crescimento_a = diferenca_a / visualizacoes[0][2]
taxa_crescimento_b = diferenca_b / visualizacoes[1][2]
if taxa_crescimento_a > taxa_crescimento_b:
    print(f"O canal {youtuber[0]} cresceu {taxa_crescimento_a / taxa_crescimento_b} vezes mais do que o canal {youtuber[1]} em termos de visualizações.")
elif taxa_crescimento_a < taxa_crescimento_b:
    print(f"O canal {youtuber[1]} cresceu {taxa_crescimento_b / taxa_crescimento_a} vezes mais do que o canal {youtuber[0]} em termos de visualizações.")
else:
    print("Os canais tiveram o mesmo crescimento em termos de visualizações.")

soma_canal_a = sum(visualizacoes_a)
soma_canal_b = sum(visualizacoes_b)
print(f"O total de visualizações do canal {youtuber[0]} nos 3 meses é {soma_canal_a}")
print(f"O total de visualizações do canal {youtuber[1]} nos 3 meses é {soma_canal_b}")