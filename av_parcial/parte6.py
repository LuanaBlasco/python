from funcoes import avalia_diferenca, avalia_taxa_crescimento

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
avalia_diferenca(visualizacoes, youtuber)
avalia_taxa_crescimento(visualizacoes, youtuber)

print("Mês 2")
visualizacoes[0].append(1000)
visualizacoes[1].append(500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][2]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][2]}")
avalia_diferenca(visualizacoes, youtuber)
avalia_taxa_crescimento(visualizacoes,youtuber)

print("Mês 3")
visualizacoes[0].append(2000)
visualizacoes[1].append(1500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][1]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][1]}")
avalia_diferenca(visualizacoes, youtuber)
avalia_taxa_crescimento(visualizacoes,youtuber)

soma_canal_a = sum(visualizacoes_a)
soma_canal_b = sum(visualizacoes_b)
print(f"O total de visualizações do canal {youtuber[0]} nos 3 meses é {soma_canal_a}")
print(f"O total de visualizações do canal {youtuber[1]} nos 3 meses é {soma_canal_b}")