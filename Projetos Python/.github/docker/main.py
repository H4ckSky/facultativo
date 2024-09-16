def ordenar_lista_vetores(lista_vetores):
    # Ordena cada vetor individualmente
    lista_vetores_ordenada = [sorted(vetor) for vetor in lista_vetores]
    
    # Ordena a lista de vetores pelo primeiro elemento de cada vetor
    lista_vetores_ordenada.sort(key=lambda x: x[0] if x else float('inf'))
    
    return lista_vetores_ordenada

lista = [[3, 2, 1, 9, 5, 6, 7, 8, 4]]
lista_ordenada = ordenar_lista_vetores(lista)
print(lista_ordenada)