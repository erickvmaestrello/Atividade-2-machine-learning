#Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos_na_lista(lista):
    primos = []
    for n in lista:
        if eh_primo(n):
            primos.append(n)
    print(primos)
    return primos
primos_na_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    