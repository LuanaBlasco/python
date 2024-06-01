anos = int(input("Preciso saber sua idade em anos, meses e dias, aqui digite quantos anos você tem: "))
meses = int(input("Agora digite os meses: "))
dias = int(input("Agora os dias: "))
anos_em_meses = anos * 12
mes = 30
total_meses = anos_em_meses + meses
total_dias = total_meses * mes
print("Você viveu %i meses" % (total_meses))
print("Sua idade em dias é %i dias " % (total_dias))
