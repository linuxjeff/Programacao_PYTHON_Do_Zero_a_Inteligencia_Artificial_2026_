nome = input("Qual é o nome do produto?\n>>> ")
preco: float = float(input("Qual o preço do produto\n>>> "))

if 20.0 <= preco <= 40.0:
    print(f"O produto {nome} foi postado com sucesso")
    print(f"O valor é de: {preco:.2f}")
else:
    print(f"O produto não foi postado, pois não esta dentro da faixa de preço.\nFaixa de preço: 20 a 40 reais")