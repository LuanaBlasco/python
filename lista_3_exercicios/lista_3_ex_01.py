import time
import random

valor_empresa_a = 98.77
valor_empresa_b = 64.32

print("\n")
print("Valor das Ações:")
print(f"A - Empresa A (R$ {valor_empresa_a:.2f})")
print(f"B - Empresa B (R$ {valor_empresa_b:.2f})")

print("\nDia 1 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

percentual_variacao = random.uniform(-3, 3)
variacao = valor_empresa_a * (percentual_variacao / 100)
valor_empresa_a += variacao

percentual_variacao = random.uniform(-3, 3)
variacao = valor_empresa_b * (percentual_variacao / 100)
valor_empresa_b += variacao

print("\nValor das Ações:")
print(f"A - Empresa A (R$ {valor_empresa_a:.2f})")
print(f"B - Empresa B (R$ {valor_empresa_b:.2f})")

print("\nDia 2 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

percentual_variacao = random.uniform(-3, 3)
variacao = valor_empresa_a * (percentual_variacao / 100)
valor_empresa_a += variacao

percentual_variacao = random.uniform(-3, 3)
variacao = valor_empresa_b * (percentual_variacao / 100)
valor_empresa_b += variacao

print("\nValor das Ações:")
print(f"A - Empresa A (R$ {valor_empresa_a:.2f})")
print(f"B - Empresa B (R$ {valor_empresa_b:.2f})")