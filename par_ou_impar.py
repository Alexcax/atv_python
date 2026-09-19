
numero = int(input("Digite um número inteiro: "))      #armazena o numero digitado pelo usuário

if numero % 2 == 0:                    #verifica se o numero é par ou ímpar, de acordo com o resto da divisão por 2        
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")