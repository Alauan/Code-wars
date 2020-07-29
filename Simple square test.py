from time import time

ini = time()
def solve(n):
    s = 0
    imparMais = 3
    imparMenos = 1
    if n % 2 or n % 4 == 0 and n > 4:
        while s != n:
            if s < n:
                s += imparMais
                imparMais += 2
            else:
                imparMenos += 2
                s -= imparMenos

        return ((imparMenos + 1)/2)**2
    else:
        return -1

n = int(input('Escolha um número   '))
print(solve(n))
'''for i in range(2, 100000):
    solve(i)'''
print(f'Tempo de execução: {time()-ini}')
