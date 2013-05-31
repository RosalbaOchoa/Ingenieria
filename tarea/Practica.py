r= [9,8,7,6]
r
[9, 8, 7, 6]
len(r)
4
# la funcion len sirve para conocer el numero de elementos
r[2]=2+2
r
[9, 8, 4, 6]
r.append('ok')
r
[9, 8, 4, 6, 'ok']
# la funcion append sirve para agregar un elemento al final de la lista


lista=['ross',10,'ing']
lista
['ross', 10, 'ing']
lista.extend(['8','7'])
lista
['ross', 10, 'ing', '8', '7']
# la funcion extend sirve para añadir elementos de otra lista, concadenar


lista.insert(3,'david')
lista
['ross', 10, 'ing', 'david', '8', '7']
# la funcion insert sirve para insertar un elemento en una posicion concreta


'ross' in lista
True
# la funcion in sirve para verificar si 'x' elementos se encuentra o no en la lista

lista.count('ing')
1
# la funcion count sirve para indicar el numero de veces que se repite un   mismo elemento


lista.reverse()
lista
['7', '8', 'david', 'ing', 10, 'ross']
lista*2
['7', '8', 'david', 'ing', 10, 'ross', '7', '8', 'david', 'ing', 10, 'ross']
# esta funcion sirve para multiplicar los elementos de una lista


del lista[3]
lista
['7', '8', 'david', 10, 'ross']
# la funcion del sirve para eliminar un elementos de la lista de 'x' posicion


lista+r
['7', '8', 'david', 10, 'ross', 9, 8, 4, 6, 'ok']
# la funcion x+x lista sirve para sumar ambas listas de elementos


r+list("pm")
[9, 8, 4, 6, 'ok', 'p', 'm']
# esta funcion permite convertir un string en una lista


p=r
r==lista
False
r==p
True
# la funcion == sirve para comparar entre listas


lista.index('ross')
4
# la funcion sirve para mostrar el indice de un elemento de una lista


lista
['7', '8', 'david', 10, 'ross']
