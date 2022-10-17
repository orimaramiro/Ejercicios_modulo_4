# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))


cantidad_numeros_positivos = 0  # Inicializo el contador en 0
cant_num_neg = 0
# for ... in range(....)
if inicio > fin:
    print ("el numero inicial debe ser menor que el fina")
if inicio < fin: 
    if inicio > 0 and fin > 0:
        cantidad_numeros_positivos = 1 # por no cantabilizar la última posición 
        for secuencia_pos in range(inicio,fin):
            cantidad_numeros_positivos += 1
    if inicio < 0 and fin < 0:
        cant_num_neg = 1
        for secuencia_neg in range(inicio,fin):
            cant_num_neg += 1
    if inicio < 0 and fin > 0:
        cantidad_numeros_positivos = 1
        for secuencia_neg in range(inicio,0):
                cant_num_neg += 1
        for secuencia_pos in (0,fin):
            cantidad_numeros_positivos += 1
print("cantidad de numeros positivos es", cantidad_numeros_positivos, "cantidad numeros negativos", cant_num_neg)
    
# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
