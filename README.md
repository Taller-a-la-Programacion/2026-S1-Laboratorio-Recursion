# 2025 Semestre 1

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio7.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación **recursiva**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**


## Convertir a Binario
Construir una función que convierta un número de base 10 a su representación en binario. Tomar en cuenta que el parámetro de entrada debe ser **entero y mayor o igual a CERO**.
Seguir las mismas reglas para la conversion, division entera, módulo y exponentes.

```python
>>>convertirBinario(2345)
100100101001
```

## Digitos ordenados
Construir una función que reciba un número e indique si sus dígitos están ordenados de manera descendente.

```python
>>>digitosOrdenados(2345678)
True
```

##	Elemento menor y mayor de la lista
Escriba un programa con sintaxis Python cuya función principal se llame **extremosLista(lista)**, que reciba como entrada una lista con números enteros denominado **lista** y que retorne la lista con 2 elementos donde ellos serán el número menor y mayor de la lista

```python
>>>extremosLista([18,5,8,45,96, 60])
[5,96]

>>> extremosLista([96, 96,96])
[96]

>>> extremosLista([])
"Error: La lista debe contener al menos 2 elementos"

>>> extremosLista([2,5,7,"ABC"])
"Error: La lista debe elementos tipo entero"
```

##	Eliminar elementos lista
Escriba un programa con sintaxis Python cuya función principal se llame **eliminarElementosLista(lista1, lista2)**, que reciba como entrada dos listas con números enteros denominado, donde **lista2** contiene los elementos a eliminar de **lista1** y que retorne la lista con los elementos eliminados

```python
>>>eliminarElementosLista([254, 25, 8], [25])
[254, 8]

>>> eliminarElementosLista([54, 25, 8], [25, 54])
[8]

>>> eliminarElementosLista([54, 25, 8], [21, 24])
[54,25,8]

>>> eliminarElementosLista([], [2,4])
"Error: La primera lista debe contener al menos 1 elemento"

>>> eliminarElementosLista([23,78,9], [])
"Error: La segunda lista debe contener al menos 1 elemento"

>>> extremosLista([2,5,7,"ABC"], [2,8])
"Error: La primera lista debe elementos tipo entero"

>>> extremosLista([2,5,7], [2,"8"])
"Error: La segunda lista debe elementos tipo entero"

```

## corrimientoAEntero(num)
Corrimientos al entero, pasar los números de la parte decimal a la parte entera.
Mantener el signo en el caso que sea negativo.
Máximo dos digitos en el decimal
No usar str() ni convertir a lista u otra función pre construida por python

```python
>>>corrimientoAEntero(133.5)   
1335
>>>corrimientoAEntero(133888.51)   
13388851
>>>corrimientoAEntero(-133.5)   
-1335
```

## cortarNumero(num, ini, fin)
Construir una función que reciba un número y ordenados de manera ascendente.
Para ambos parámetros solo números enteros positivos.
Verificar que los parámtros **ini** y **fin** no sobre pasen el largo del número.
```python
>>>cortarNumero(1335, 1, 2)
33
>>>cortarNumero(1335, 8, 2)
'Error: Indices fuera del rango del número'
```
