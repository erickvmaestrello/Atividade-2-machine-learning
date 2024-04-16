#Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def impares(lista):
    impares = []
    for n in lista:
        if n % 2 != 0:
            impares.append(n)
    return impares
print(impares([1, 2, 3, 4, 5]))
