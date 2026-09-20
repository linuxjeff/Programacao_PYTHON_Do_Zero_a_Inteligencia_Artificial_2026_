from funcoes import verificarMaiorIdade

quantosAnos = int(input('Qual a sua idade?\n>>> '))

if verificarMaiorIdade(quantosAnos):
    print(f'Você tem {quantosAnos} anos.\nVocê é maior de idade.')
else:
    print(f'Você tem {quantosAnos} anos.\nVocê é menor de idade.')
