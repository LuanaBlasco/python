import random
def simula_variacao_uma_empresa(cotacao_atual):
    valor_percentual = random.uniform(-3, 3)
    variacao_percentual = valor_percentual * cotacao_atual
    nova_cotacao = variacao_percentual + cotacao_atual
    return nova_cotacao

def simula_variacao_uma_empresa2(cotacoes_empresas):
    valor_percentual = random.uniform(-3, 3)
    variacao_percentual = valor_percentual * cotacoes_empresas
    nova_cotacao = variacao_percentual + cotacoes_empresas
    return nova_cotacao

def imprime_empresas(empresas, cotacoes_empresas):
    print()
    for i in range(len(empresas)):
        print(f"Cotação empresa {empresas[i]}: {cotacoes_empresas[i]}")

def simula_variacoes(cotacoes_empresas):
    novas_cotacoes = []
    for i in range(len(cotacoes_empresas)):
        novas_cotacoes.append(simula_variacao_uma_empresa2(cotacoes_empresas[i][-1]))
    return novas_cotacoes

def simula_variacoes2(cotacoes_empresas):
    for i in range(len(cotacoes_empresas)):
        cotacoes_empresas[i].append(simula_variacao_uma_empresa2(cotacoes_empresas[i][-1]))

def imprime_empresas2(empresas, cotacoes_empresas):
    print()
    for i in range(len(empresas)):
        print(f"Cotação empresa {empresas[i]}:")
        print([f"{valor:.2f}" for valor in cotacoes_empresas[i]])


