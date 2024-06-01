from variacao import simula_variacao_uma_empresa, simula_variacoes, simula_dia_investimento

valor_empresa_a = 98.77
valor_empresa_b = 64.32

valores_empresas = [valor_empresa_a, valor_empresa_b]

def imprime_valores(valores):
    print("\nValor das Ações:")
    for i in range(len(valores)):
        print(f"{chr(65+i)} - Empresa {chr(65+i)} (R$ {valores[i]:.2f})")

imprime_valores(valores_empresas)

for dia in range(1, 6):
    valores_empresas = simula_dia_investimento(dia, valores_empresas)
    imprime_valores(valores_empresas)
