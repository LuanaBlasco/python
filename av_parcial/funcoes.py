def avalia_diferenca(visualizacoes, youtuber):
    for i in range(len(youtuber)):
        diferenca = visualizacoes [i][-1] - visualizacoes[i][-2]
        if i ==0:
            diferenca_a = diferenca
        else:
            diferenca_b = diferenca
            if diferenca_a > diferenca_b:
                print(f"O canal {youtuber[0]} teve {diferenca_a-diferenca_b} visualizações a mais do que o canal {youtuber[1]}")
            elif diferenca_a < diferenca_b:
                print(f"O canal {youtuber[1]} teve {diferenca_b-diferenca_a} visualizações a mais do que o canal {youtuber[0]}")
            else:
                print("Os canais tiveram a mesma quantidade de visualizações.")


def avalia_taxa_crescimento(visualizacoes, youtuber):
    for i in range(len(youtuber)):
        taxa_crescimento = (visualizacoes[i][-1] - visualizacoes[i][-2]) / visualizacoes[i][-2]
        if i == 0:
            taxa_crescimento_a = taxa_crescimento
        else:
            taxa_crescimento_b = taxa_crescimento
            if taxa_crescimento_a > taxa_crescimento_b:
                print(f"O canal {youtuber[0]} cresceu {taxa_crescimento_a / taxa_crescimento_b} vezes mais do que o canal {youtuber[1]} em termos de visualizações.")
            elif taxa_crescimento_a < taxa_crescimento_b:
                print(f"O canal {youtuber[1]} cresceu {taxa_crescimento_b / taxa_crescimento_a} vezes mais do que o canal {youtuber[0]} em termos de visualizações.")
            else:
                print("Os canais tiveram o mesmo crescimento em termos de visualizações.")



