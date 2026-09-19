# Conversor de Tempo em formato de relogio digital, porque eu não sabia qual das duas formas o senhor queria.

segundos_totais = 12345                                         #armazena os segundos

minutos, segundos = divmod(segundos_totais, 60)                 #divide os segundos para saber os minutos e os segundos restantes
horas, minutos = divmod(minutos, 60)                            #divide os minutos para saber as horas e os minutos restantes

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")              #dois formatos de prints para ficar bonito
print(f"{horas}h {minutos}m {segundos}s")