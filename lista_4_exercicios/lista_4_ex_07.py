from funcoes import simula_variacao_uma_empresa2, imprime_empresas2, simula_variacoes2
cotacoes_empresa_a = []
cotacoes_empresa_b = []
cotacoes_empresas = [cotacoes_empresa_a, cotacoes_empresa_b]
empresas = ['A', 'B']


cotacoes_empresas[0].append(100.00)
cotacoes_empresas[1].append(80.00)
imprime_empresas2(empresas, cotacoes_empresas)


simula_variacoes2(cotacoes_empresas)
imprime_empresas2(empresas, cotacoes_empresas)


simula_variacoes2(cotacoes_empresas)
imprime_empresas2(empresas, cotacoes_empresas)

simula_variacoes2(cotacoes_empresas)
imprime_empresas2(empresas, cotacoes_empresas)
