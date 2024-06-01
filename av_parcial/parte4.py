from funcoes import avalia_diferenca

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


print("Mês 2")
visualizacoes[0].append(1000)
visualizacoes[1].append(500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][2]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][2]}")
avalia_diferenca(visualizacoes, youtuber)


print("Mês 3")
visualizacoes[0].append(2000)
visualizacoes[1].append(1500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][1]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][1]}")
avalia_diferenca(visualizacoes, youtuber)