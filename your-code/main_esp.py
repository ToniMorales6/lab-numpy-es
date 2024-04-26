#1. Importa el paquete NUMPY bajo el nombre np.

#[tu código aquí]
import numpy as np

#2. Imprime la versión de NUMPY y la configuración.
print("2. Imprime la versión de NUMPY y la configuración.")
#[tu código aquí]
print(np.version.version)

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?
print("3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable a")
#[tu código aquí]
a = np.random.rand(2,3,5)
print(a)
a = np.random.random((2,3,5))

#4. Imprime a.
print("4. Imprime a")
#[tu código aquí]
print(a)
#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"
print("5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.")
#[tu código aquí]
b = np.ones((5,2,3))
#6. Imprime b.
print("6. Imprime b")
#[tu código aquí]
print(b)

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?
print("7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?")
#[tu código aquí]
if (a.size == b.size):
    print("a y b tienen el mismo tamaño")
    print("Se demuestra comparando ambos sizes a.size == b.size")
else: print("a y b no tienen el mismo tamaño")

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?
print("8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?")
#[tu código aquí]
if (a.shape == b.shape):
    print("es posible sumar a y b")
else: print("no es posible sumar a y b")
#se podrian sumar si tuviesen la misma shape, se prueba con una matriz c
c = b.reshape((2,3,5))
print(a.shape == c.shape)
#c si que se podría sumar con a



#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".
print("9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable c.")
#[tu código aquí]
print(a.shape, '-', b.shape)
c = np.transpose(b, axes=(1, 2, 0))
print(a.shape, '-', c.shape)
if (a.shape == c.shape):
    print("es posible sumar a y c")
else: print("no es posible sumar a y c")
#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?
print("10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable d. Pero, ¿por qué funciona ahora?")
#[tu código aquí]
d = a + c
#funciona porque tienen la misma shape

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.
print("11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.")
#[tu código aquí]
print(d)
print(a)


#12. Multiplica a y c. Asigna el resultado a e.
print("12. Multiplica a y c. Asigna el resultado a e.")
#[tu código aquí]
e = a * c
print(e)


#13. ¿Es e igual a a? ¿Por qué sí o por qué no?
print("13. ¿Es e igual a a? ¿Por qué sí o por qué no?")
#[tu código aquí]
print(e.size == a.size)
print(e.shape == a.shape)
#e es igual a, ya que cuando se multiplican no se varia la forma ni la composoción, solo se multiplican los valores escalarmente



#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"
print("14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables d_max, d_min y d_mean")
#[tu código aquí]
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print(f"{d_max} valor maximo, {d_min} valor minimo, {d_mean} media")

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.
print("15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío f con la misma forma (es decir, 2x3x5) que d usando `np.empty`.")
#[tu código aquí]
f = np.empty((2, 3, 5))
print(f)


"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

#[tu código aquí]
it = np.nditer(d, flags=['multi_index'])
while not it.finished:
    if it[0] == d_min:
        f[it.multi_index] = 0
    elif d_min < it[0] < d_mean:
        f[it.multi_index] = 25
    elif it[0] == d_mean:
        f[it.multi_index] = 50
    elif d_mean < it[0] < d_max: 
        f[it.multi_index] = 75
    else:
        f[it.multi_index] = 100
    it.iternext()


"""
#17. Imprime d y f. ¿Tienes el f esperado?
Por ejemplo, si tu d es:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Tu f debería ser:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print('17. Imprime d y f. ¿Tienes el f esperado?')
#[tu código aquí]
print('D')
print(d)
print(f"{d_max} valor maximo, {d_min} valor minimo, {d_mean} media")
print('F')
print(f)



"""
#18. Pregunta de bonificación: en lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena 
("A", "B", "C", "D" y "E") para etiquetar los elementos del array? Esperas el resultado sea:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
De nuevo, no necesitas Numpy en esta pregunta.
"""
print("""18. Pregunta de bonificación: en lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena 
(A, B, C, D y E) para etiquetar los elementos del array?""")
#[tu código aquí]
g = np.empty((2, 3, 5), dtype=str)
it = np.nditer(d, flags=['multi_index'])
while not it.finished:
    if it[0] == d_min:
        g[it.multi_index] = "A"
    elif d_min < it[0] < d_mean:
        g[it.multi_index] = "B"
    elif it[0] == d_mean:
        g[it.multi_index] = "C"
    elif d_mean < it[0] < d_max: 
        g[it.multi_index] = "D"
    else:
        g[it.multi_index] = "E"
    it.iternext()

print("G")
print(g)