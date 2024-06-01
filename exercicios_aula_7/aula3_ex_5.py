import math
graus = float(input("Informe o valor em graus para um ângulo: (somente números) " ))
radianos = graus * (math.pi/180)
seno = math.sin(graus)
cosseno = math.cos(graus)
tangente = math.tan(graus)
print("O para o valor de %i graus, em radianos é %f, o seno é %f, o cosseno é %f e a tangente é %f" % (graus, radianos, seno, cosseno, tangente))


