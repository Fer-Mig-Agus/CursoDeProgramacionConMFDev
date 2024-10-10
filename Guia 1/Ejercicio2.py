# 2- Leer tres números en las variables A, B y C, realizar los siguientes cálculos e imprimir los resultados:
# a- La suma de los tres
# b- La diferencia del primero respecto del segundo
# c- El producto de los dos últimos
# d- La división entre el primero y el tercero


A=int(input('Ingrese el valor a: '))
B=int(input('Ingrese el valor b: '))
C=int(input('Ingrese el valor c: '))


suma=A+B+C
resta=A-B
producto=B*C

if C != 0:
    division=A/C
    print("El resultado de la division es: ",division)
else:
    print("No se puede dividir por cero")


print("La suma es: ",suma)
print("La resta es: ",resta)
print("El producto es: ",producto)



