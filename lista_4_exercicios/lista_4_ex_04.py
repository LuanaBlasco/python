from funcoes import simula_variacao_uma_empresa2

cotacoes_empresa_a = []
cotacoes_empresa_b = []
cotacoes_empresas = [cotacoes_empresa_a, cotacoes_empresa_b]

cotacoes_empresas[0].append(100.00)
cotacoes_empresas[1].append(80.00)


print()
print(f"Cotação A: {cotacoes_empresas[0]} ")
print(f"Cotação A: {cotacoes_empresas[1]} ")

nova_cotacao_a = simula_variacao_uma_empresa2(cotacoes_empresas [0][-1])
nova_cotacao_b = simula_variacao_uma_empresa2(cotacoes_empresas[1][-1])

cotacoes_empresas[0].append(nova_cotacao_a)
cotacoes_empresas[1].append(nova_cotacao_b)

print()
print(f"Cotação A: {cotacoes_empresas[0]}")
print(f"Cotação A: {cotacoes_empresas[1]}")

