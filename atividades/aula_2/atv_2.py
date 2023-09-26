value = int(input("Informe o total de segundos: "))

hours = value / 3600
minutes = (value - (hours * 3600)) / 60
seconds = value % 60

print(f"{value} convertidos em hora, minuto e segundos é igual a: {hours:.0f}:{minutes:.0f}:{seconds:.0f}")
