import random
import time

def simula_variacao_uma_empresa(valor):
    percentual_variacao = random.uniform(-3,3)
    variacao = valor * (percentual_variacao/100)
    valor += variacao
    return valor

def simula_variacoes(valores):
    for i in range(len(valores)):
        valores[i] = simula_variacao_uma_empresa(valores[i])
    return valores


def simula_dias(dia):
    print(f"\nDia {dia} ", end="", flush=True)
    for i in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)

def simula_dia_investimento(dia, valores):
    simula_dias(dia)
    valores = simula_variacoes(valores)
    return valores
