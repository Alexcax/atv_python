
valorseg = 1200                                #variavel que armazena o valor em segundos

horas = (valorseg / 3600)                      #variaveis que fazem a transformação de segundos para horas e minutos
minutos = (valorseg / 60)

print(f"{valorseg} segundos equivalem a {horas:.2f} horas e {minutos:.2f} minutos.")