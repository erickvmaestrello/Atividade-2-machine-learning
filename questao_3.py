#Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def listas(lista1, lista2):
    num1 = set (lista1)
    num2 = set (lista2)
    elementos = list(num1.symmetric_difference(num2))
    elementos.sort()
    return elementos
print (listas([10, 20, 30, 40], [30, 40, 50, 60]))
