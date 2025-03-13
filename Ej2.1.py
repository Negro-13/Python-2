print('Ingrese numeros enteros positivos')
number = int(input())
count = 0
while number > -1:
    count += number
    number = int(input())

print(f'El resultado es {count}')