# 6- Dado un número que representa la cantidad de lados de un polígono, determinar si se trata de un triángulo,
# cuadrilátero o de un pentágono; en caso de no tratarse de una de estas figuras, imprimir un mensaje

lados=int(input("Ingrese los lados: "))

match lados:
    case 3:
        print("Triangulo")
    case 4:
        print("cuadrilátero")
    case 5:
        print("pentágono")
    case _:
        print("Dato inválido")
