import math

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))
delta = b**2-4*a*c
raizdelta = delta ** (1/2)
print("raiz de delta é igual a: %.2f" % (raizdelta))
x1 = (-b+raizdelta) /(2*a)
print("x1 é : %.2f " % (x1))
x2 = (-b-raizdelta) /(2*a)
print("x2 é : %.2f " % (x2))