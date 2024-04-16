#Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundo_maior(lista):
    lista = list(set(lista))
    if len(lista) < 2:
        return None
    lista.sort()
    return lista[-2]
print(segundo_maior([1, 2, 3, 4, 5]))