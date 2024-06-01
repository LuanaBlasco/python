import random
from funcoes import simula_variacao_uma_empresa

cotacoes_empresa_a = []
cotacoes_empresa_b = []
cotacao_atual = [cotacoes_empresa_a, cotacoes_empresa_b]

cotacoes_empresa_a.append(100.00)
cotacoes_empresa_b.append(80.00)

print()
print(f"Cotação empresa A: {cotacoes_empresa_a}")
print(f"Cotações empresa B: {cotacoes_empresa_b}")


nova_cotacao_a = simula_variacao_uma_empresa(cotacoes_empresa_a[-1])
nova_cotacap_b = simula_variacao_uma_empresa(cotacoes_empresa_b[-1])

cotacoes_empresa_a.append(nova_cotacao_a)
cotacoes_empresa_b.append(nova_cotacap_b)

print()
print(f"Cotação empresa A: {cotacoes_empresa_a}")
print(f"Cotações empresa B: {cotacoes_empresa_b}")

