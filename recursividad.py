#recursividad
'''
def pares(n, limite):
    print(2*n)
    pares(n+1,limite)
pares(0,100)
'''#error de recursividad
'''
def pares(n, limite):
    if n < limite:
        print(2*n)
        pares(n+1,limite)
pares(0,100)
'''#si tiene limite
'''
def searchbin():
    if len(lst) == 0:
        return False
    mid = lst[len(lst)/2]
    if n == mid:
        return True
    elif n < mid:
        return searchbin(n, lst[:len(lst)//2])
    elif n > mid:
        return searchbin(n, lst[len(lst)//2+1]:)
lst = [8,9,6,7,2,3,6,4,5,2,3,6,4,6,2,6,748,56]
print("esta en la lista el valor 5?", searchbin())
'''#busqueda binaria d un numero por recursividad
