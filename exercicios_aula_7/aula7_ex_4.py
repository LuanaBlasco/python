seg = int(input("Digite uma quantidade em segundos: "))

horas = seg // 3600
seg_rest = seg % 3600
minutos = seg_rest // 60
seg_rest = seg_rest % 60

print("A quantidade de %i segundos equivale a %i horas, %i minutos e %i segundos " % (seg, horas, minutos, seg_rest ))
