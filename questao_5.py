#Crie uma função que receba uma lista de tuplas, cada uma contendo o
#nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
#pessoas em ordem alfabética.

def lista_de_tuplas(lista):
    lista_ordenada = sorted(lista, key=lambda x: x[0])
    print (lista_ordenada)
    return lista_ordenada
lista_de_tuplas([('Ana', 23), ('João', 20), ('Carlos', 25), ('Elon', 39), ('Day', 31)])
