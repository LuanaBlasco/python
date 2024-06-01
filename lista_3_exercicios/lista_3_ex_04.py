import time
from variacao import simula_variacao_uma_empresa, simula_variacoes

valor_empresa_a = 98.77
valor_empresa_b = 64.32
valor_empresa_c = 75.89

valores_empresas = [valor_empresa_a, valor_empresa_b, valor_empresa_c]

def imprime_valores(valores):
    print("\nValor das Ações:")
    for i in range(len(valores)):
        print(f"{chr(65+i)} - Empresa {chr(65+i)} (R$ {valores[i]:.2f})")

def simula_dia(dia):
    print(f"\nDia {dia} ", end="", flush=True)
    for i in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)

imprime_valores(valores_empresas)

for dia in range(1, 5):
    simula_dia(dia)
    valores_empresas = simula_variacoes(valores_empresas)
    imprime_valores(valores_empresas)
