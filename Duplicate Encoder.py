code = list()


def duplicate_encode(word):
    for i in word:
        if word.count(i) > 1:
            code.append(')')
        else:
            code.append('(')
    return code


palavra = str(input('Coloque a sua palavra para ser codificada aqui:'))
print(''.join(duplicate_encode(palavra)))
