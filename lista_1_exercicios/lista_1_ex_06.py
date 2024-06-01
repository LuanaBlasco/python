print("Conversão de Temperatura")
c = int(input("Informe os Graus em Celcius(somente números): "))
f = (c*1.8) + 32
k= c + 273.15
print("A temperatura de %i graus Celsius equivale a %f Fahrenheit e %f Kelvin" % (c,f,k))