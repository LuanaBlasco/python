import time
from variacao import simula_variacao_uma_empresa, simula_variacoes

valor_empresa_a = 98.77
valor_empresa_b = 64.32
valor_empresa_c = 75.89

valores_empresas = [valor_empresa_a, valor_empresa_b, valor_empresa_c]

print("\nDia 1 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

def imprime_valores():
    print("\nValor das Ações:")
    print(f"A - Empresa A (R$ {valores_empresas[0]:.2f})")
    print(f"B - Empresa B (R$ {valores_empresas[1]:.2f})")
    print(f"C - Empresa C (R$ {valores_empresas[2]:.2f})")

imprime_valores()

print("\nDia 2 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)


valores_empresas = simula_variacoes(valores_empresas)

imprime_valores()
