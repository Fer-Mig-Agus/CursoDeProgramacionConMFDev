# 7- Dados tres números A, B y C imprimir el mayor de ellos

A=int(input('Ingrese el valor a: '))
B=int(input('Ingrese el valor b: '))
C=int(input('Ingrese el valor c: '))

if A>B and A>C:
    print('El mayor es A')
else:
    if B > C:
        print('El mayor es B')
    else:
        print('El mayor es C')

