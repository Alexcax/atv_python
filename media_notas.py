
nota1 = float(input("Digite a primeira nota: "))               
nota2 = float(input("Digite a segunda nota: "))                    #variaveis que armazenam as notas no formato float, para notas como 8.5, 7.5, etc.
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3                                #calcula a média das notas
print(f"A média das notas é: {media:.2f}")                         #exibe a média das notas com duas casas decimais