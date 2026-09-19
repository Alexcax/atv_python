
preco_produto = 100                     #armazena o preço do produto

desconto = 0.2                          #armazena o valor do desconto (20% neste caso)

preco_com_desconto = preco_produto - (preco_produto * desconto)               #calcula o preço do produto com desconto
print(f"O preço do produto com desconto é: R${preco_com_desconto:.2f}")