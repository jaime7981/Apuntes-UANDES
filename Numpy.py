#numphy es Es una biblioteca que permite trabajar con datos numéricos en espacios multidimensionales.
from numpy import *
#NumPy introduce dos nuevos tipos de datos que permiten representar vectores y matrices

#Array: Se usa para almacenar vectores.
#Un array se puede crear a partir de una lista
'''
list = [124, 577, 5657, 655]

arr = array(list)
print(list)
print(arr)
'''
#se puede realizar aritmética básica con array y escalares
'''print(3*arr+2)'''
#
#poner funciones de array ppt
#
#Como veremos más adelante, linspace(min, max, cantidad) es muy útil para crear gráficos de funciones
'''
valores = linspace(10,30,20)
print(valores)
print(valores[0], valres[19])
'''
#un subarray siempre toma referencias a los elementos de la lista original.
#Se puede crear una copia de un array usando la operación arr.copy()
'''
arr2 = arr.copy()
arr2[0] = 133
print(arr, arr2)
'''
#
#poner funciones aritmeticas y otras funciones de array sec 13.2
#

#matrices
#Una matriz (matrix en numpy) se puede entender como un array bidimensional.
'''
mat = matrix([1,2,3],[4,5,6],[7,8,9]) #Se puede crear una matriz utilizando una lista de listas.
print(mat)
print(mat*2)
print(mat*mat)7
print(mat**2)
'''
#Podemos saber la cantidad de filas de una matriz usando la función len() que ya conocemos.
#Sin embargo, para saber la cantidad de columnas, len()no sirve.
#La forma correcta de conocer las dimensiones de una matriz es con la propiedad shape.
'''print(mat.shape)''' #(fila,columna)

#multiplicar matrices
#El número de columnas de A debe coincidir con el número de filas de B.
'''
mat1 = matrix([[1,2,3],[4,5,6]])
mat2 = matrix([7,8],[9,10],[11,12])
print(mat1*mat2)
'''

#sistema de ecuaciones
#Con NumPy podemos resolver sistema de ecuaciones lineales de N variables y N ecuaciones, es decir, de NxN.

#matplotlib
from matplotlib import pyplot
#plyplot.axis() configura los ejes del gráfico
#.plot() dibuja el gráfico en la ventana de gráfico
#.subplot() dibuja un subgráfico
#.show() muestra el gráfico
#.clf() limpia la ventana de gráficos
#Se requieren conjuntos de datos para la abscisa y la ordenada.
#Una lista (o array) para la abcisa.
#Otra lista (o array) para la ordenada.
'''
valores = [2,6,3,7,8,4,2,4,5]
pyplot.plot(valores)
pyplot.show()
'''#con una lista con x tomando valor de len(valores)
'''
cx = [1,2,8,3,-5]
cy = [7,3,8,5,1]
if len(cx) == len(cy):
    pyplot.plot(cx,cy)
    pyplot.show()
'''#con lista para x e y del mismo largo

#gráfico de funciones
#evalua la funcion en un rango de puntos
#El rango de valores generado con linspace es un array.
'''
x = arrange(11)
pyplot.plot(x, cos(x))
pyplot.show()
'''

#grafico de barras
#Los gráficos de barras requieren una secuencia de valores, en donde cada valor representa la altura de una columna (o barra).
#Necesitamos los valores de las columnas a graficar y una secuencia de valores con las alturas de las columnas.
'''
columnas = range(6)
valores = [5,6,4,2,7]
pyplot.bar(columnas, valores)
pyplot.show()
'''# se usa pyplot.bar()

#histogramas
#Un histograma permite visualizar frecuencia de valores por rango.

alturas = [5,6,8,2,4,5]
pyplot.hist(alturas)
pyplot.show()
# se usapyplot.hist()

#coordenadas polares
#En el plano polar, cada punto lo caracterizamos por su distancia al origen y el ángulo que forma con el eje referencial.
#Usamos la operación pyplot.polar(),pasando como parámetros el ángulo (en radianes) y el radio (distancia al origen) deseado.
'''
import numpy as np # se especifica la libreria de la funcion
t  = np.linspace(0, 2*no.pi, 1000)
r = 2*t
pyplot.polar(t, r)
pyplot.show()

r = np.cos(t)
pyplot.polar(t, r)
pyplot.show()

r = -1*np.cos(t)
pyplot.polar(t, r)
pyplot.show()
'''
#Podemos dar formato a las curvas de un gráfico usando opciones (parámetros) de las funciones de pyplot
