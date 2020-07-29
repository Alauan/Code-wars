sequencia = list()


def josephus(items, k):
    num = 0
    for i in range(1, len(items)+1):
        num = (num - 1 + int(k)) % len(items)
        sequencia.append(items[num])
        items.pop(num)
    return sequencia


print(josephus([],3))
