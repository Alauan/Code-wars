def dig_pow(n, p):
    x = 0
    for i in range(0, len(str(n))):
        x += int(str(n)[i])**(int(p)+i)
    k = x/int(n)
    if k.is_integer():
        return k
    else:
        return -1
n = input('coloque uma valor para n: ')
p = input('coloque uma valor para p: ')
print('k é', dig_pow(n, p))