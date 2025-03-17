names = []
print('Ingrese un nombre a la lista')
name = input()
while name != 'fin':
    names.append(name)
    name = input()
alfa = names.sort()

names.sort
print(f'Tu lista es: {names}')

count = 0
index = 0
while index < len(names):
    if names[index].lower()[0] == 'a':
        count += 1
        index += 1
    else:
        index += 1



print(f'La cantidad de nombre q comienzan con A y E son {count}')