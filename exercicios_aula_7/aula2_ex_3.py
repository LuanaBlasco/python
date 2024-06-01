distancia = float(input("Informe a distancia entre as cidades em km/h : "))
tempo_horas = float(input("Digie as horas do tempo percorrido: "))
tempo_minutos = float(input("Digite os minutos do tempo percorrido: ")) 
conv_minutos = tempo_minutos / 60
tempo = tempo_horas + conv_minutos
vm = distancia / tempo
print("A velocidade média permitida de uma distância de %.2f Km/h no tempo de %.2f /h é de %.2f km/h " % (distancia, tempo, vm))
