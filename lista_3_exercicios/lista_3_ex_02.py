import time
from variacao import simula_variacao_uma_empresa


valor_empresa_a = 98.77
valor_empresa_b = 64.32
valor_empresa_c = 75.89

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
    print(f"A - Empresa A (R$ {valor_empresa_a:.2f})")
    print(f"B - Empresa B (R$ {valor_empresa_b:.2f})")
    print(f"C - Empresa C (R$ {valor_empresa_c:.2f})")

imprime_valores()

print("\nDia 2 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

valor_empresa_a = simula_variacao_uma_empresa(valor_empresa_a) 
valor_empresa_b = simula_variacao_uma_empresa(valor_empresa_b)
valor_empresa_c = simula_variacao_uma_empresa(valor_empresa_c)
imprime_valores()