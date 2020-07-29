string = input("Digite uma equação   ")
lista = string.split()
comeco = 0
final = 0


def solvemult():
    n1 = lista[comeco: final].index('*') + comeco - 1
    n2 = n1 + 2
    lista[n1 + 1] = float(lista[n1]) * float(lista[n2])
    lista.pop(n2)
    lista.pop(n1)
def solvediv():
    n1 = lista[comeco: final].index('/') + comeco - 1
    n2 = n1 + 2
    lista[n1 + 1] = float(lista[n1]) / float(lista[n2])
    lista.pop(n2)
    lista.pop(n1)
def solvesub():
    n1 = lista[comeco: final].index('-') + comeco - 1
    n2 = n1 + 2
    lista[n1 + 1] = float(lista[n1]) - float(lista[n2])
    lista.pop(n2)
    lista.pop(n1)
def solveadd():
    n1 = lista[comeco: final].index('+') + comeco - 1
    n2 = n1 + 2
    lista[n1 + 1] = float(lista[n1]) + float(lista[n2])
    lista.pop(n2)
    lista.pop(n1)

while len(lista) != 1:
    if '(' in string:
        for indice, v in enumerate(lista):
            if v == '(':
                comeco = indice + 1
            elif v == ')':
                final = indice - 1
                if comeco == final:
                    lista.pop(comeco + 1)
                    lista.pop(comeco - 1)
    else:
        comeco = 0
        final = len(lista) - 1

    if '*' in lista[comeco: final] and '/' in lista[comeco: final]:
        if lista.index('*') < lista.index('/'):
            solvemult()
        else:
            solvediv()

    elif '*' in lista[comeco: final]:
        solvemult()
    elif '/' in lista[comeco: final]:
        solvediv()

    elif '+' in lista[comeco: final] and '-' in lista[comeco: final]:
        if lista.index('+') < lista.index('-'):
            solveadd()
        else:
            solvesub()

    elif '+' in lista[comeco: final]:
        solveadd()
    elif '-' in lista[comeco: final]:
        solvesub()

print(lista[0]).
