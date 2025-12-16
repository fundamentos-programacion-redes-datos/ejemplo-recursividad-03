# Esta función requiere que la lista esté ORDENADA
def busqueda_binaria_recursiva(lista, objetivo, inicio, fin):
    # 1. CASO BASE: Si el rango de búsqueda es inválido, el elemento no está.
    if inicio > fin:
        return -1  # Retorna -1 si no se encuentra

    # Calcular el punto medio
    medio = (inicio + fin) // 2

    # 2. CASO BASE: Encontramos el objetivo
    if lista[medio] == objetivo:
        return medio

    # 3. LLAMADAS RECURSIVAS (el problema se reduce a la mitad)
    else:
        if lista[medio] < objetivo:
            # El objetivo está en la mitad derecha
            return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
        else:
            # El objetivo está en la mitad izquierda
            return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)


numeros_ordenados = [11, 31, 33, 44, 55, 66]
buscar = 31

indice = busqueda_binaria_recursiva(
    numeros_ordenados, buscar, 0, len(numeros_ordenados) - 1
)

if indice != -1:
    print(f"El número {buscar} se encontró en el índice {indice}.")
