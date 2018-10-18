#tuplas
(a,b,c) = (1,2,3) #no puede cambiar
x = list(a,b,c) #transforma una tupla en lista
#diccionarios
#cualquier objeto puede actuar como índice
#loa elementos se guardan con asociaciones
<clave,valor> #no hay relación secuencial
              #la clave no se puede repetir, son únicas
dn = {}

dn2 = {"clave":"valor", "clave2":"valor2","una tupla":("a","b","c")}

clave2 = dn2["clave2"] #asigna "valor2"

tupla = dn2["una tupla"][1] #devuelve "b"
#si el elemento no existe, python tira error

dn["c-013"] = "miercolesxdxd" #crea una nueva clave "c-013" con su valor "miercolesxdxd"

dn.pop("c-013") #elimina la clave

for clave in dn2:
    print(dn2[clave])#imprime cada clave de un diccionario

ks = dn2.keys() #junta toda las claves en un conjunto de claves
ks = list(ks) #convierte el conjunto d claves en una lista
