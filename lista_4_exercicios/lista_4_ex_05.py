from funcoes import simula_variacao_uma_empresa2, imprime_empresas, simula_variacoes

cotacoes_empresa_a = []
cotacoes_empresa_b = []
cotacoes_empresas = [cotacoes_empresa_a, cotacoes_empresa_b]
empresas = ['A', 'B']

cotacoes_empresas[0].append(100.00)
cotacoes_empresas[1].append(80.00)

imprime_empresas(empresas, cotacoes_empresas)

novas_cotacoes = simula_variacoes(cotacoes_empresas)

cotacoes_empresas[0].append(novas_cotacoes[0])
cotacoes_empresas[1].append(novas_cotacoes[1])

imprime_empresas(empresas, cotacoes_empresas)
novas_cotacoes = simula_variacoes(cotacoes_empresas)


