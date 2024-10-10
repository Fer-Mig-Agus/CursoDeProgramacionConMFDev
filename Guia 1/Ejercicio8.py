# 8- Dados 100 números, realizar la suma de los positivos y de los negativos.

c=1
sumaP=0
sumaN=0

N=int(input('Ingrese la cantidad de numeros: '))

while c <= N:
    num=int(input('Ingrese el numero: '))
    if num > 0:
        sumaP=sumaP+num
        # sumaP+=num
    else:
        sumaN+=num
    c+=1

print('La suma de lo positivos es: ',sumaP)
print('La suma de lo negativos es: ',sumaN)
