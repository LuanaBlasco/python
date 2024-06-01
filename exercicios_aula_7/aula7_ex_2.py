alunos = 0 
eleitores = 0 
nao_eleitores = 0
idade_nao_eleitores = 0
while alunos <= 500:
    alunos += 1
    idade = int(input("Qual é sua idade ? "))
    if idade >= 16:
        eleitores = eleitores + 1
    else:
        nao_eleitores = nao_eleitores + 1
        idade_nao_eleitores = idade_nao_eleitores + idade

    media_idade_nao_eleitores = idade_nao_eleitores / nao_eleitores if nao_eleitores > 0 else 0 
    print("Entre os %i alunos, %i são eleitores e %i não são eleitores" % (alunos, eleitores, nao_eleitores))
    print("A média da idade dos não-eleitores: ", media_idade_nao_eleitores)
    sair = input("Deseja sair ? (s/n) ")
    if sair == "s" or sair == "S":
        break