<h1>Aprendiendo Python con <a href='https://www.youtube.com/@MFDev-yz1bw' target='_blank'>MF Dev</a> </h1>

## Que es Python?

Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

## Donde lo puedo usar?

Python es también usado para fines muy diversos como son los siguientes:

•	Desarrollo Web: Existen frameworks como Django, Pyramid, Flask o Bottle que permiten desarrollar páginas web a todos los niveles.

•	Ciencia y Educación: Debido a su sintaxis tan sencilla, es una herramienta perfecta para enseñar conceptos de programación a todos los niveles. En lo relativo a ciencia y cálculo numérico, existen gran cantidad de librerías como SciPy o Pandas.

•	Desarrollo de Interfaces Gráficos: Gran cantidad de los programas que utilizamos tienen un interfaz gráfico que facilita su uso. Python también puede ser usado para desarrollar GUIs con librerías como Kivy o pyqt.

•	Desarrollo Software: También es usado como soporte para desarrolladores, como para testing.

•	Machine Learning: En los último años ha crecido el número de implementaciones en Python de librerías de aprendizaje automático como Keras, TensorFlow, PyTorch o sklearn.

•	Visualización de Datos: Existen varias librerías muy usadas para mostrar datos en gráficas, como matplotlib, seaborn o plotly.

•	Finanzas y Trading: Gracias a librerías como QuantLib o qtpylib y a su facilidad de uso, es cada vez más usado en estos sectores

# Sintaxis

## Comentario

Para colocar un comentario en Python, hacer uso del: `#` seguido del comentario. 
Ejemplo:

```py
# Esto es un Comentario
```
Tambien podemos hacer uso de las comillas simples: `'` , pero necesitamos 3 al inicio y 3 al final, esto nos permite poner varias lineas de comentario.
Ejemplo
```py
'''
Esto es un comentario
de varias lineas
y no hay problema
'''
```

#### Atajo de teclado en VS Code
Para realizar colocar como comentario una o varias lineas, basta con seleccionar la porcion de codigo con el mouse, para luego precionar esta combiacion de teclas:

1: `Ctrl` + `k`

2: `Ctrl` + `c`

Para descomentar, podemos usar esta combinacion de teclas:

1: `Ctrl` + `k`

2: `Ctrl` + `u`


## Definicion de Variables


En otro lenguajes es necesario especificar que x almacenará un valor entero, pero no es el caso. Python es muy listo y al ver el número 5, sabrá de que tipo tiene que ser la x.

Ejemplo:

```py
x=5 # Tipo Int
```
```py
x='a' # Tipo Chart
```
```py
x='hola' # Tipo String
```
```py
x=7.5 # Tipo Float
```

## Palabras reservadas

![alt text](https://res.cloudinary.com/dgp4xwknu/image/upload/v1728586246/Certificados/pjzzrxlasrgix7wrklb1.png)

## Operadores

![alt text](https://res.cloudinary.com/dgp4xwknu/image/upload/v1728586246/Certificados/dm55oufcvnqdpha7douw.png)

## Ingreso de datos

Para ingresar datos debemos de usar la palabra reservada `input` seguido de un pequeño mensaje.

Ejemplo:

```py
name=input('Ingrese el nombre: ')
```

El valor dato que se guardara sera en formato `String`, pero si queremos otro tipo de dato, vamos a `convertirlo`, colocando antes del `input` el tipo de dato.

Ejemplo:

```py
age=int(input('Ingrese la edad: ')) # Tipo int
```

```py
weight=float(input('Ingrese el peso: ')) # Tipo float
```

## Impresion

Para imprimir, haremos uso de la palabra reservada: `print` , podemos usarlo de varias maneras, dependiendo el uso que le querramos dar

Ejemplo:

```py
print('Hola mundo') # Salida: Hola mundo
```

Usando una variable podemos hacer asi:

Ejemplo:

```py
x='MF Dev'
print(x) # Salida: MF Dev
```

```py
age=26
print('Tu edad es: ',age) # Salida: Tu edad es: 26
```

```py
name='MF dev'
age=26
print('Hola ',name,' tu edad es ',age) # Salida: Hola MF Dev tu edad es 26
```

Podemos ir formateando tambien

Ejemplo:

```py
message = "La edad es "
age = 25
print(message + str(age))
```

```py
name = "La edad es"
age = 25
print(f"{name} {age}")
```

```py
name = "La edad es"
age = 25
print("{} {}".format(name, age))
```

```py
name = "La edad es"
age = 25
print("%s %d" % (name, age))

```

Sientete libre de usar el que mas te guste

## Condicional

En todo buen programa, vamos a necesitar hacer condiciones por lo que para eso tenemos el queridisimo `if` con su buen compañero `else` , ambos nos ayudan a hacer condiciones junto con los operadores

Ejemplo:

```py
x=5
if x == 5:
    print('Si es el numero 5')
else:
    print('No es el numero 5')
```

Ten cuidado!!! El `else` no hace condiciones, por lo que si colocar el siguiente codigo esta mal:

Ejemplo:

```py
x=5
if x == 5:
    print('Si es el numero 5')
else x== 6:
    print('Es el numero 6')
```
Esto esta mal, es un sacrilegio hacer eso, cuando tenemos varias condiciones, podemos hacer uso del buen `elif` que basicamente es un `else` con un `if` anidados

#### Usando elif
```py
x=5
if x == 5:
    print('Si es el numero 5')
elif x == 6:
    print('Si es el numero 6')
elif x == 7:
    print('Si es el numero 7')
elif x == 8:
    print('Si es el numero 8')
else:
    print('No es ningun numero')

```
#### Usando if anidados
```py
x=5
if x == 5:
    print('Si es el numero 5')
else:
    if x == 6:
        print('Es el numero 6')
    else:
        if x == 7:
            print('Es el numero 7')
        else:
            print('No es ningun numero')
```

Como puedes observar el `elif` no ayuda a tener una mejor comprension del codigo, con solo pegar un pequeño vistaso, en cambio el `if` anidado es mucho mas engorroso y torpe para analizar.

## Condiciones dobles

Muchas veces tenemos que hacer dos condiciones, o mas, depende mucho de el como lo vayas a plantear. Para ello es muy importante el hacer uso de los operados logicos, en otros lenguajes tenemos que el operador `Y` se representa de esta manera: `&&` pero en **Python** lo hacemos asi: `and`. Pasa lo mismo con el operados `O`, en otros lenguajes se representa asi: `||` pero en **Python** lo haremos asi: `or`. Cabe aclarar que las dobles condiciones las podemos hacer dentro de un `if` o `elif`, pero **JAMAS** sobre un `else`, el else no lleva condicion.

Ejemplo:

* Implementado el `and`

```py
value=int(input('Ingrese un numero: '))
if value >= 6 and value <= 10:
    print('Estas entre el 6 y el 10')
else:
    print('Estas fuera del rango')
```

* Implementando el `or`
```py
value=int(input('Ingrese un numero: '))
if value < 10 or value > 99:
    print('No eres de dos digitos')
else:
    print('Eres de dos digitos')
```

## Switch Case

Muchas veces necesitamos hacer un programa donde dependiendo de una condiciones haremos tal cosa, si bien podemos usar los `if anidados` o el `elif` existe algo aun mas sencillo, llamado `swtich case`, cabe destacar que en otros lenguajes lo vas a encontrar con este nombre, pero en el caso de Python lo encontraras de la siguiente manera.

Ejemplo:


```py
dia=int(input("Ingrese el dia: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Día inválido")

```

## Bucles

Muchas veces tenemos que hacer una tarea muchas veces, para ello podemos optar por usar un `bucle`, tambien conocido como `iterador`. Existen varios:
* While
* For
* Do while
* Repeat Until

Vamos a ver a cada uno, pero antes debes de saber que el `do while` no existe en python, pero era importante que lo conoscas por que si existe en otros lenguajes, dicho eso empecemos.


## Bucles: *while*

Consta de un contador y un valor limite, de esta manera cuando ya no cumpla la condicion es que el bucle va a terminar.

Ejemplo:

```py
count = 0
while count < 5:
    print("El contador es:", count)
    count += 1
```


## Bucles: *repeat until*
Si bien Python no tiene la estructura del repeat until, nosotros podemos simularlo.

Ejemplo:

```py
count = 0
while True:
    print("El contador es:", count)
    count += 1
    if count >= 5:  # Condición de salida
        break
```

## Bucles: *for*

Se utiliza cuando sabemos cuántas veces queremos que el bucle se repita.
```py
for i in range(5):
    print("Valor de i:", i)
```

También puedes usar for para recorrer elementos de una lista.
```py
lista = ["manzana", "banana", "cereza"]
for fruta in lista:
    print("Fruta:", fruta)
```

Si necesitas tanto el índice como el valor, puedes usar enumerate().
```py
lista = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(lista):
    print(f"Fruta en el índice {indice}: {fruta}")
```

Si queremos terminar el bucle podemos hacer uso del `break` o si queremos que continue usaremos `continue`

```py
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    if i % 2 == 0:
        continue  # Salta los números pares
    print(i)
```

## Funciones incorporadas

Python tiene funciones propias, las cuales podemos hacer uso cuando nosotros dispongamos, algunas estan por defecto, pero otras tenemos que importar una libreria para hacer uso de la misma.

## Funciones incorporadas: Defecto

##### len()
```py
texto = "Hola mundo"
longitud = len(texto)
print(longitud)  # Salida: 10
```
##### type()
```py
numero = 42
tipo = type(numero)
print(tipo)  # Salida: <class 'int'>
```
##### abs()
```py
numero = -15
absoluto = abs(numero)
print(absoluto)  # Salida: 15
```
##### round()
```py
numero = 3.14159
redondeado = round(numero, 2)
print(redondeado)  # Salida: 3.14
```
##### max()
```py
numeros = [3, 5, 7, 2, 8]
maximo = max(numeros)
print(maximo)  # Salida: 8
```
##### min()
```py
numeros = [3, 5, 7, 2, 8]
minimo = min(numeros)
print(minimo)  # Salida: 2
```
##### sum()
```py
numeros = [1, 2, 3, 4, 5]
suma = sum(numeros)
print(suma)  # Salida: 15
```
##### sorted()
```py
numeros = [5, 3, 8, 6, 1]
ordenados = sorted(numeros)
print(ordenados)  # Salida: [1, 3, 5, 6, 8]
```

## Funciones incorporadas: Importacion

##### sqrt()
```py
import math

numero = 16
raiz = math.sqrt(numero)
print(raiz)  # Salida: 4.0
```
##### randint()
```py
import random

aleatorio = random.randint(1, 10)
print(aleatorio)  # Salida: un número entre 1 y 10
```
##### datetime.now()
```py
from datetime import datetime

ahora = datetime.now()
print(ahora)  # Salida: fecha y hora actual
```
##### choise()
```py
import random

opciones = ['manzana', 'banana', 'cereza']
seleccion = random.choice(opciones)
print(seleccion)  # Salida: un elemento aleatorio de la lista
```
##### DataFrame()
```py
import pandas as pd

datos = {'Nombre': ['Juan', 'María', 'Pedro'], 'Edad': [28, 34, 22]}
df = pd.DataFrame(datos)
print(df)

# Salida
'''
   Nombre  Edad
0   Juan    28
1  María    34
2  Pedro    22

'''
```

## Funciones: *Propias*

Nosotros vamos a necesitar crear nuestra propias funciones, para ello vamos a hacer uso de la palabra reservada `def` seguido del nombre de la funcion, luego parentesis `()` seguido de dos puntos `:`

Ejemplo:

```py
def miFuncion():
    print('Mi primera funcion')
```

Pero tambien tenemos que saber sobre los `parametros` de una funcion, existen dos tipos: 

* Parametro formal: Es la que se define en cuanto se crea la funcion

* Parametro actual: El el que se envia a la funcion en tiempo de ejecucion

Ejemplo:

```py
def esPositivo(value):
    if value > 0:
        return True
    else:
        return False

# Llamo a la funcion
number=6
retorno=esPositivo(number)

if retorno:
    print('Es positivo')
else:
    print('Es negativo')

```

Aqui podemos ver que el parametro formal es `value` pero el parametro actual es `number`, con esto quiero dejar en claro que no es necesario que tengan el mismo nombre, porque lo que importa es el valor.
Una vez claro eso, tenemos dos maneras en que se "pasan" los argumentos, puede ser `por valor` y `por referencia`.

#### Argumento por valor:
* En el paso por valor, se pasa una copia del valor del argumento a la función.

* Cualquier modificación que se haga dentro de la función no afecta la variable original fuera de la función.

* Esto es común con tipos de datos inmutables (como números, strings, tuplas en Python).

Ejemplo:

```py
def incrementar(x):
    x += 1
    print("Dentro de la función:", x)

num = 5
incrementar(num)
print("Fuera de la función:", num)

# Salida
'''
Dentro de la función: 6
Fuera de la función: 5
'''
```

#### Argumento por referencia:
* En el paso por referencia, se pasa la referencia (es decir, la dirección en memoria) del objeto a la función.

* Cualquier modificación realizada en el objeto dentro de la función afecta directamente al objeto original, ya que ambos apuntan al mismo lugar en memoria.

* Esto ocurre con tipos de datos mutables (como listas, diccionarios, conjuntos en Python).

Ejemplo:

```py
def agregar_elemento(lista):
    lista.append(4)
    print("Dentro de la función:", lista)

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
print("Fuera de la función:", mi_lista)

#Salida
'''
Dentro de la función: [1, 2, 3, 4]
Fuera de la función: [1, 2, 3, 4]
'''
```

