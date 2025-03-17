palabra = input('Ingrese una cadena: ')
count = 0
index = 0
while index < len(palabra):
    if palabra.lower()[index] == 'a':
        count += 1
        index += 1
    else:
        index += 1

print({count})
