# 4- Leer dos números, almacenarlos en las variables X y Y respectivamente. Intercambiar el contenido de las variables


x=int(input('Ingrese el valor de X: '))
y=int(input('Ingrese el valor de Y: '))

aux=x
x=y
y=aux

print('nuevo valor de X= ',x)
print('nuevo valor de Y= ',y)

