fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('Ingrese una fruta para agregar a la lista:')
new = input()
fruits.append(new)

index = 0
print('Las frutas de la lista son:')
while index < len(fruits):
    print(fruits[index])
    index += 1

