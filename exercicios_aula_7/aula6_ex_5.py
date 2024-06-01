mulheres = 0
homens = 0
altura_mulheres =0
altura_homens = 0

while True:
    genero = input("Qual seu gênero? ('F' para feminino, 'M' para masculino ou escreva 'sair' para terminar: )")
    if genero == "sair":
            print("Altura média das mulheres:", altura_media_mulheres)
            print("Altura média dos homens:", altura_media_homens)
            break

    altura = float(input("Digite sua altura em metros: "))
    if genero == "F" or genero == "f":
        mulheres = mulheres + 1
        altura_mulheres += altura
    elif genero == "m" or genero == "M":
        homens += 1
        altura_homens += altura
    
    altura_media_mulheres = altura_mulheres / mulheres if mulheres > 0 else 0 
    altura_media_homens = altura_homens / homens if homens > 0 else 0
    print("Altura média das mulheres:", altura_media_mulheres)
    print("Altura média dos homens:", altura_media_homens)









        



        


