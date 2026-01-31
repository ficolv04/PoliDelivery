def ordenar_burbuja(lista, llave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][llave] > lista[j + 1][llave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Algoritmo Quick Sort 
def quick_sort(lista, llave):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2][llave]
    izquierda = [x for x in lista if x[llave] < pivote]
    centro = [x for x in lista if x[llave] == pivote]
    derecha = [x for x in lista if x[llave] > pivote]
    return quick_sort(izquierda, llave) + centro + quick_sort(derecha, llave)