#Realizar operaciones de unión, intersección y diferencia
#de conjuntos
#Tenemos los siguientes conjutnos:
c1 = {0, 1, 2, 3, 4, 5, 6}
c2 = {0, 2, 4, 6, 8, 10}
c3 = {0, 1, 2, 3}
#UNION
Union = c1.union(c2)
print("La union de de los conjuntos c1 y c2: ",Union)
#INTERSECCION
Interseccion = c1.intersection(c2)
print("La interseccion de de los conjuntos c1 y c2: ",Interseccion)
#DIFERENCIA
Diferencia = c1.difference(c2)
print("La Diferencia de de los conjuntos c1 y c2: ",Diferencia)

#Calcular la diferencia entre dos conjuntos
#Diferencia entre 3 conjuntos:

Interseccion = c1.intersection(c2,c3)
print("La interseccion de de los conjuntos c1, c2 y c3: ",Interseccion)

#Calcular la diferencia simétrica entre 3 conjuntos
D_Simetrica = c1.symmetric_difference(c2,c3)
print("La Diferencia simetrica de de los conjuntos c1, c2 y c3: ",D_Simetrica)