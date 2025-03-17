fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

buscar = input('Que fruta quiere buscar en la lista:')
index = 0

while index < len(fruits):
    if buscar.lower() == fruits[index]:
        print(f'Se a encontrado la fruta {buscar}')
        index += len(fruits) + 1
    else:
        index += 1

if index == len(fruits):
    print(f'No se encontro la futa {buscar}')
